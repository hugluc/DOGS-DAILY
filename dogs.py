import requests
import time
from fake_useragent import UserAgent
from datetime import datetime
import sys

fake_useragent = UserAgent()

url = "https://api.onetime.dog/rewards"

# Membaca user_ids dari file tgid.txt
with open('tgid.txt', 'r') as file:
    user_ids = file.read().splitlines()

# Mendapatkan waktu saat ini
current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")

for user_id in user_ids:
    user_agent = fake_useragent.random

    params = {
        'user_id': user_id
    }

    headers = {
        'User-Agent': user_agent,
        'Accept': "application/json",
        'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://onetime.dog",
        'x-requested-with': "org.telegram.messenger",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://onetime.dog/",
        'accept-language': "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
        'if-modified-since': current_time,
        'priority': "u=1, i"
    }

    print(f"Sending request for user_id {user_id} with User-Agent: {user_agent}")
    sys.stdout.flush()  # Ensure the print statement is output immediately
    response = requests.get(url, params=params, headers=headers)

    print(f"Response for user_id {user_id}:")
    print(response.text)
    sys.stdout.flush()  # Ensure the print statement is output immediately
    print("\n" + "="*50 + "\n")
    sys.stdout.flush()  # Ensure the print statement is output immediately

    # Menambahkan delay 5 detik setelah setiap permintaan
    delay_time = 5
    print("Start")
    for i in range(5):
        print(f"Waiting... {i + 1}")
        time.sleep(1)
        print("Done")
