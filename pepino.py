import requests
import time
import telegram

# Replace the API key and chat ID with your own
TOKEN = "5723647924:AAEr7fodamyolFNJW7NGjqIlgjYEScmeuwY"
CHAT_ID = "1613266416"

# Define the Bybit API endpoint
API_ENDPOINT = "https://api.bybit.com/v2/public/tickers?symbol=1000PEPEUSDT"

# Create the Telegram bot
bot = telegram.Bot(token=TOKEN)

while True:
    try:
        # Retrieve the price from Bybit
        response = requests.get(API_ENDPOINT)
        data = response.json()
        price = float(data["result"][0]["last_price"])
        
        # Send the price to the Telegram channel
        message = f"PEPE {price:.10f} USD"
       await bot.send_message(chat_id=CHAT_ID, text=message)

        
    except Exception as e:
        print(f"Error: {e}")
        
    # Wait for 1 second before sending the next message
    time.sleep(1)
