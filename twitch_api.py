import urllib.parse
import urllib.request
import json

'''
https://api.twitch.tv/kraken/streams/riotgames?client_id=8dc5w9ciwi4s8e224uz14qfh2jmm96a
https://api.twitch.tv/kraken/streams/[channel]?client_id=8dc5w9ciwi4s8e224uz14qfh2jmm96a
'''

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
print(get_result('https://twitch.tv/riotgames'))