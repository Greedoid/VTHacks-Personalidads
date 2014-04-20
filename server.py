# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import sys
import pprint
from pyechonest import song, artist
from config import *
from pyechonest import config
import oauth2 as oauth
import urllib
from rdio import Rdio
import json
import pyen
from genre import *
from personality import *
import logging
from logging.handlers import RotatingFileHandler

class rdio_simple:

	def __init__(self, CK, CS):
		self.rdio_obj = Rdio((CK, CS))

	def get_user_key_from_name(self, user_name):
		name = self.rdio_obj.call("findUser", {"vanityName": user_name})
		return name['result']['key']

	def get_collection_from_key(self, key):
		collection = self.rdio_obj.call("getTracksInCollection", {"user":key, "extras":"playCount"})
		return collection
	
	def get_artists_from_collection(self, collection):
		my_list = []
		for item in collection['result']:
			my_list.append(item['artist'].encode('utf-8'))
		return my_list

app = Flask(__name__)
config.ECHO_NEST_API_KEY = ECHO_NEST_API_KEY
global_shitshow = GLOBAL_SHITSHOW

def make_artist_dict(artist_collection):
	artist_dict = {}
	for i in range (0, len(artist_collection)-1):
		if artist_collection[i] in artist_dict:
			artist_dict[artist_collection[i]] = artist_dict[artist_collection[i]] + 1
		else:
			artist_dict[artist_collection[i]] = 1
	return artist_dict


def make_genre_dict(artist_dict):
	genre_dict = {}
	for key, value in artist_dict.iteritems():
		art = artist.Artist(key, buckets = ['genre'])
		for item in art.cache['genres']:
			if item['name'] in genre_dict:
				genre_dict[item['name']] = genre_dict[item['name']] + value
			else:
				genre_dict[item['name']] = value
	return genre_dict

def get_first_global_genre(similarity_object):
	for item in similarity_object:
		if item['name'] in global_shitshow:
			return item

def map_subgenres_to_shitshow(genres):
	turn_dict_for_what = {}
	en = pyen.Pyen(ECHO_NEST_API_KEY)
	for key, value in genres.iteritems():
		if key not in global_shitshow:
			response = en.get('genre/similar', name=key)
			gen = get_first_global_genre(response['genres'])
			if gen is not None:
				turn_dict_for_what[key] = gen['name'] 
		else:
			turn_dict_for_what[key] = key
	return turn_dict_for_what

def swap_subgenres_to_genres(subgenres, mapping):
	fuckit = {}
	for key, value in subgenres.iteritems():
		if key in mapping:
			if mapping[key] in fuckit:
				fuckit[mapping[key]] += value
			else:
				fuckit[mapping[key]] = value
	return fuckit

@app.route("/")
def func():
	return render_template("index.html")

@app.route("/demo", methods=['POST', 'GET'])
def demo():
	name = request.args.get('name')
	if name is None:
		return redirect("/", code=302)
	return render_template("demo.html")

@app.route("/demoJSON", methods=['POST', 'GET'])
def demoJSON():
	name = request.args.get('name')
	if name is None:
		return "{}"
	artist_dict = {}
	genre_dict = {}
	r_d = rdio_simple(CONSUMER_KEY, CONSUMER_SECRET)
	key = r_d.get_user_key_from_name(name)
	collection = r_d.get_artists_from_collection(r_d.get_collection_from_key(key))
	genre_dict = make_genre_dict(make_artist_dict(collection))
	dictString = {"name":"interpolator", "children":[{'name':key,"size":(int(value))} for key,value in genre_dict.items()]}
	data = str(json.dumps(dictString))
	mapping = map_subgenres_to_shitshow(genre_dict)
	swappedDict = swap_subgenres_to_genres(genre_dict, mapping)
	print swappedDict.keys()
	print "Finding personality............"
	finalList = personality(swappedDict)
	personalityDict = {}
	personalityDict['Extraversion'] = str(round(finalList[0],2))
	personalityDict['Agreeableness'] = str(round(finalList[1],2))
	personalityDict['Conscientiousness'] = str(round(finalList[2],2))
	personalityDict['Neuroticism'] = str(round(finalList[3],2))
	personalityDict['Openness'] = str(round(finalList[4],2))
	personalityString = [{'name':key,"size":value} for key,value in personalityDict.items()]
	#finalJSON = "{'data':"+data+", 'values':[{axis:'Extraversion', value:"+str(round(finalList[0], 2))+"},{axis:'Agreeableness', value:"+str(round(finalList[1], 2))+"},{axis:'Conscientiousness', value:"+str(round(finalList[2], 2))+"},{axis:'Neuroticism', value:"+str(round(finalList[3], 2))+"},{axis:'Openness',value:"+str(round(finalList[4], 2))+"}]}"
	#finalJSON = "{'data':"+data+", 'values':{"+str(json.dumps(personalityString)) +"}}"
	#finalJSON = "{'data':"+data+"}"
	blah = {}
	blah['data'] = dictString
	blah['values'] = personalityString
	#blah['data'] = genre_dict
	#blah['values'] = personalityDict
	return json.dumps(blah)

if __name__ == "__main__":
	handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	app.run(host='0.0.0.0', debug=True)
