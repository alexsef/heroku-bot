import requests
import json
from time import sleep

token = '664459261:AAHLepXGT1QDoG6eE13uequX9TDvM0E7IN0'
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():
	data = get_updates()

	last_object = data['result'][-1]
	current_update_id = last_object['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id
		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']

		message = {'chat_id': chat_id,
				   'text': message_text}

		return message
	return None


def send_message(chat_id, text):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)


def main():
	# while True:
	# 	answer = get_message()

	# 	if answer != None:
	# 		chat_id = answer['chat_id']
	# 		text = answer['text']

	# 		if 'привет' in text:
	# 			send_message(chat_id, 'Hello ' + text)
	# 	else:
	# 		continue

	# 	sleep(5)
	# get_message()
	d = get_updates()

	with open('updates.json', 'w') as file:
		json.dump(d, file, indent=2)


if __name__ == '__main__':
	main()



