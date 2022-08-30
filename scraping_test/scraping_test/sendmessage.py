import requests
from time import time


token = '5661801778:AAGYBFfze7-Hk_ZS20k9VUwOW98vTlyJGmk'
chat_id = '-751877560'
time = time


def sendTelegram(text):
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id' : chat_id,
        'text' : text,
        'time': time
    })

