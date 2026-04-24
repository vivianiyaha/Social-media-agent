import requests
import os

FB_TOKEN = os.getenv("FB_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"

    data = {
        "message": message,
        "access_token": FB_TOKEN
    }

    response = requests.post(url, data=data)
    print("Facebook response:", response.json())
