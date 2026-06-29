from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("Missing env")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

@app.route("/", methods=["GET"])
def home():
    return "BOT LIVE", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    signal = data.get("signal", "UNKNOWN")
    ticker = data.get("ticker", "N/A")

    msg = f"Signal: {signal}\nTicker: {ticker}"

    send_message(msg)

    return {"status": "ok"}, 200