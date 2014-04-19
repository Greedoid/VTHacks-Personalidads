import oauth2 as oauth
import urllib
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


def main():

	r_d = rdio_simple(CONSUMER_KEY, CONSUMER_SECRET)
	key = r_d.get_user_key_from_name("Greedoid")
	r_d.get_tracks_from_collection(r_d.get_collection_from_key(key))


'''
	consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
	client = oauth.Client(consumer)
	response = client.request('http://api.rdio.com/1/', 'POST', urllib.urlencode({'method': 'get', 'keys': 's3505267'}))
	print response[1]

	print get_user_key_from_name('Greedoid')
'''


if __name__ == "__main__":
	main()
