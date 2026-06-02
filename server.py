"""
server.py — Flask сервер для birthday сайта
Нужен только если используешь локальный video.mp4 (не YouTube).

Установка:  pip install flask
Запуск:     python3 server.py
Телефон:    http://192.168.X.X:8000  (та же WiFi-сеть)
Render:     gunicorn server:app
"""
from flask import Flask, send_from_directory, Response
import os, mimetypes

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))

# Поддержка Range-запросов (нужна для перемотки видео на iOS)
@app.route("/")
def index():
    return send_from_directory(ROOT, "birthday.html")

@app.route("/<path:filename>")
def serve(filename):
    path = os.path.join(ROOT, filename)
    if not os.path.exists(path):
        return "Not found", 404
    mime, _ = mimetypes.guess_type(path)
    # Range support для видео
    range_header = app.request_class.environ.get  # placeholder
    return send_from_directory(ROOT, filename, mimetype=mime, conditional=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    print(f"""
  Сервер запущен!
  Компьютер:  http://localhost:{port}
  Телефон:    http://{ip}:{port}   (та же WiFi-сеть)
  Стоп:       Ctrl+C
""")
    app.run(host="0.0.0.0", port=port, debug=False)
