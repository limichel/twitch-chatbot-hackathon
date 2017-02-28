HOST = 'irc.chat.twitch.tv'
PORT = 6667

PASSWORD = 'oauth:ngv7o14obgerlfmfbiwmtxw6izaq1x' # Password (OAuth token)
USERNAME = 'lemonmochi'
CHANNEL = 'alwaysfailinginlife'

from socket_setup import Socket
import random
import time
import deviantart_twitch_api

# ideas to allow ppl to interact with it
# artbot?

irc_connection = Socket()

irc_connection.connect(HOST, PORT) # Attempts to connect to the host/port (in this case, Twitch IRC)

print('Connection successful. Logging in...')

# Sends log in information
irc_connection.send_message('PASS {}\r\n'.format(PASSWORD))
irc_connection.send_message('NICK {}\r\n'.format(USERNAME))
# Joins a channel's chat
irc_connection.send_message('JOIN #{}\r\n'.format(CHANNEL))

print(irc_connection.receive_response())


# json_stream_result = deviantart_twitch_api.get_result(
# 	deviantart_twitch_api.build_stream_url('riotgames'))
# game = ''
# if json_stream_result['stream'] != None:
# 	game = json_stream_result['stream']['game']

url = deviantart_twitch_api.build_search_url('League of Legends')
print(url)

all_search_results = []

json_search_result = deviantart_twitch_api.get_result(url)

for obj in json_search_result['results']:
	if not obj['is_mature']:
		all_search_results.append(obj['url'])

while json_search_result['has_more'] == True and len(all_search_results) <= 250:
	extended_url = url + '&offset=' + str(json_search_result['next_offset'])
	json_search_result = deviantar_ttwitch_api.get_result(extended_url)
	for obj in json_search_result['results']:
		if not obj['is_mature']: # only show a picture if it's SFW
			all_search_results.append(obj['url'])
print(all_search_results)



while True:
	irc_connection.send_message('PRIVMSG #{} :Random fan creation! {}\r\n'.format(CHANNEL, 
		all_search_results[random.randint(0, len(all_search_results))]))
	time.sleep(20) # every 5 minutes, choose a random (popular) piece of art to post in chat

irc_connection.close_socket()