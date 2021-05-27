from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json

APIKey = 'GGMG7UQJDG1FF36QK4DSPUJ78M8DCZ6RUH'

u = Updater('1693468140:AAGksGkaKQBjP7MllxOcEjddWcBYNjWkKQ8', use_context=True)#token of the bot
j = u.job_queue
def callback_minute(context : CallbackContext):
	result = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + APIKey).json()['result']
	Safe, Propose, Fast = int(result['SafeGasPrice']), int(result['ProposeGasPrice']), int(result['FastGasPrice'])
	context.bot.send_message(chat_id='-582933990', text='low|avg|high\n' + Safe + Propose + Fast)

job_minute = j.run_repeating(callback_minute, interval=60, first=10)
u.start_polling()
u.idle()
