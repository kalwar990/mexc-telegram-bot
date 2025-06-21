import requests
import time

BOT_TOKEN = '7265759366:AAELk4P9fWzDb0X0mWBWplTWiO28cuMPCdA'
CHAT_ID = '-1002679659476'

def send_signal():
    message = """
📢 MEXC Spot Signal Bot Connected!
✅ Real-time alerts are now LIVE.
📈 Pre-pump breakout signals will now be sent here.
"""
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

# Send the message once
send_signal()

while True:
    time.sleep(600)
  
