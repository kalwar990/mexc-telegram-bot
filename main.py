import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SIGNAL_FEED_URL = 'https://signal-flow-mexc.onrender.com/api/spot-latest'

def get_latest_signal():
    print("🔄 Fetching signal...")
    try:
        res = requests.get(SIGNAL_FEED_URL, timeout=10)
        if res.status_code == 200:
            signal = res.json().get('signal')
            print("✅ Signal received:", signal)
            return signal
        else:
            print("❌ Bad response:", res.status_code)
    except Exception as e:
        print("🚨 Signal fetch error:", e)
    return None

def send_to_telegram(message):
    print("📤 Sending to Telegram...")
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        res = requests.post(url, data=payload)
        print("📬 Telegram response:", res.status_code)
    except Exception as e:
        print("❌ Telegram send error:", e)

last_sent = None
print("🚀 Bot started... Waiting for signal.")

while True:
    signal = get_latest_signal()
    if signal and signal != last_sent:
        send_to_telegram(signal)
        last_sent = signal
    time.sleep(30)
    
