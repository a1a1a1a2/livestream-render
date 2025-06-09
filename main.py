from flask import Flask
from ffmpeg_stream import start_stream

app = Flask(__name__)

@app.route("/")
def home():
    return "🟢 Livestream bot is running!"

@app.route("/start")
def start():
    start_stream()
    return "🎬 Livestream started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
