import requestsimport jsonfrom time import sleepfrom flask import Flaskfrom flask import requestfrom flask import jsonifyimport randomimport matplotlib.pylab as pltimport numpy as npimport scheduleimport timeapp = Flask(__name__)telegram_token = '664459261:AAHLepXGT1QDoG6eE13uequX9TDvM0E7IN0'URL = 'https://api.telegram.org/bot' + telegram_token + '/'def main():	schedule.every().day.at("23:35").do(job, 'It is 01:00')	while True:		schedule.run_pending()		time.sleep(2)  # wait one minutedef job(t):	print ("I'm working..." + t)	returndef get_updates():	url = URL + 'getupdates'	r = requests.get(url)	return r.json()def get_message():	data = get_updates()	last_object = data['result'][-1]	current_update_id = last_object['update_id']	global last_update_id	if last_update_id != current_update_id:		last_update_id = current_update_id		chat_id = last_object['message']['chat']['id']		message_text = last_object['message']['text']		message = {'chat_id': chat_id,				   'text': message_text}		return messagedef send_message(chat_id, text):	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)	requests.get(url)if __name__ == '__main__':	main()