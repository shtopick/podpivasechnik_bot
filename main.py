import requests
import time
from pprint import pprint

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6598248184:AAFz9h0Keo_OrNr33nQjWc7eRrteaOjt_Wk'
TEXT = 'Пиво льется через край'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    pprint(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1