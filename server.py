from flask import Flask, render_template
import oauth2 as oauth
import urllib
import json
from rdio import Rdio
import pyechonest
from config import CONSUMER_KEY, CONSUMER_SECRET


class rdio_simple:

	def __init__(self, CK, CS):
		self.rdio_obj = Rdio((CK, CS))

	def get_user_key_from_name(self, user_name):
		name = self.rdio_obj.call("findUser", {"vanityName": user_name})
		return name['result']['key']

	def get_collection_from_key(self, key):
		collection = self.rdio_obj.call("getTracksInCollection", {"user":key})
		return collection
	
	def get_tracks_from_collection(self, collection):
		for item in collection['result']:
			print item['name']
		return collection

app = Flask(__name__)

@app.route("/")
def func():
	return render_template("index.html")

@app.route("/demo")
def demo():
	r_d = rdio_simple(CONSUMER_KEY, CONSUMER_SECRET)
	key = r_d.get_user_key_from_name("Greedoid")
	return json.dumps(r_d.get_tracks_from_collection(r_d.get_collection_from_key(key)), ensure_ascii=False)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
