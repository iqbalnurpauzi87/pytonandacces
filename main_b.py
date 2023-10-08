import requests
# Your user ID: 1586166338
# Current chat ID: 1586166338

import requests
import time
from datetime import datetime

def send_to_telegram(message):

    apiToken = '1613209666:AAFT_0VnhMW6pquy4n2RhnVwOySyMNymTq0'
    chatID = '1586166338'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
time.sleep(10)

for x in range(15):
    time.sleep(1)
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    date_time = str(date_time)
    y = str(x)
    data_kirim = str(date_time + "  --  " + y)

    send_to_telegram(data_kirim)