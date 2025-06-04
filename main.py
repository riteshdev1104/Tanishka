
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Tanishka Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    # Telegram handling logic will go here
    return "OK"

@app.route("/admin")
def admin():
    return "Admin panel placeholder"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
