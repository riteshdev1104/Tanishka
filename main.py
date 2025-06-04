
from flask import Flask, request, render_template, redirect
import os
import requests

BOT_TOKEN = "7642244008:AAFgHQ8Mflq1T3eQkFcwV0amfwnCfw018Eg"

app = Flask(__name__)

@app.route("/")
def home():
    return "Tanishka Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    # Telegram handling logic placeholder
    return "OK"

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/send", methods=["POST"])
def send():
    chat_id = request.form.get("chat_id")
    message = request.form.get("message")
    if chat_id and message:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        requests.post(url, data=data)
    return redirect("/admin")

if __name__ == "__main__":
    port_str = os.environ.get("PORT", "5000")
    try:
        port = int(port_str)
    except ValueError:
        port = 5000
    app.run(host="0.0.0.0", port=port)
        
