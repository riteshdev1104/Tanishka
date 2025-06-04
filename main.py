
from flask import Flask, request, render_template, redirect
import os
import requests
import time
import threading

BOT_TOKEN = "7642244008:AAFgHQ8Mflq1T3eQkFcwV0amfwnCfw018Eg"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(f"{API_URL}/sendMessage", data={"chat_id": chat_id, "text": text})

@app.route("/")
def home():
    return "Tanishka Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_msg = data["message"].get("text", "")
        threading.Thread(target=reply_like_girl, args=(chat_id, user_msg)).start()
    return "OK"

def reply_like_girl(chat_id, user_msg):
    cute_responses = [
        "aww really? 🥺",
        "tum bahut cute ho 😳",
        "hehe 😅 kya baat hai!",
        "hmm... interesting 🤔",
        "ab kya bolun main 🥰",
        "tumse baat karke acha lagta hai 💬",
        "arre wah! 😍"
    ]
    # Simulate typing delay
    time.sleep(2)
    send_message(chat_id, "typing... 🤫")
    time.sleep(2)
    from random import choice
    reply = choice(cute_responses)
    send_message(chat_id, reply)

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/send", methods=["POST"])
def send():
    chat_id = request.form.get("chat_id")
    message = request.form.get("message")
    if chat_id and message:
        send_message(chat_id, message)
    return redirect("/admin")

if __name__ == "__main__":
    port_str = os.environ.get("PORT", "5000")
    try:
        port = int(port_str)
    except ValueError:
        port = 5000
    app.run(host="0.0.0.0", port=port)
