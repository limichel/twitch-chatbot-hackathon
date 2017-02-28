import urllib.parse
import urllib.request
import json

BASE_DA_SEARCH_URL = 'https://www.deviantart.com/api/v1/oauth2/browse/popular?'
BASE_TWITCH_STREAM_URL = 'https://api.twitch.tv/kraken/streams/'

# https://www.deviantart.com/api/v1/oauth2/browse/popular?q=overwatch&timerange=alltime&access_token=c7fec2f773f18d74e8cf204ee557487765d7498cfd236f5803

'''
https://www.deviantart.com/api/v1/oauth2/browse/popular?q=[game]
&timerange=alltime&access_token=49ea9e54367f99284b8a40cc4dd462072cd49a280c35357f34
'''

def build_search_url(game: str) -> str:
	'''Takes a str respresenting the name of a game and returns a URL that can be used to ask
	the deviantArt API for search results'''
	query_parameters = [('q', game), ('timerange', 'alltime'), ('limit', '120'), 
	('access_token', '49ea9e54367f99284b8a40cc4dd462072cd49a280c35357f34')]
	return BASE_DA_SEARCH_URL + urllib.parse.urlencode(query_parameters)

def build_stream_url(channel: str) -> str:
	'''Takes a str representing the name of a Twitch channel and returns a URL that can be used 
	to ask the Twitch API for details about the channel/stream'''
	query_parameters = [('client_id', '8dc5w9ciwi4s8e224uz14qfh2jmm96a')]
	return BASE_TWITCH_STREAM_URL + channel + '?' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json':
	'''Takes a URL and returns a Python object representing the parsed JSON response'''
	response = None
	try:
		response = urllib.request.urlopen(url)
		json_text = response.read().decode(encoding = 'utf-8')
		return json.loads(json_text)
	finally:
		if response != None:
			response.close()

