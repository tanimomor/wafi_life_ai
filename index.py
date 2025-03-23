import requests

url = "http://13.202.138.225:5678/webhook-test/bot"

data = {
    "message": "Order status ki: orderno: 1129210, phone: 01858544666",
   
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Request sent successfully!")
    print("Response:", response.json())  # You can inspect the response
else:
    print("Error:", response.status_code)