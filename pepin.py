import asyncio
import requests
import bybit
from dotenv import load_dotenv
import os

load_dotenv()

# Replace the API key and chat ID with your own
TOKEN = os.environ.get("5723647924:AAEr7fodamyolFNJW7NGjqIlgjYEScmeuwY")
CHAT_ID = os.environ.get("1613266416")

# Create the Bybit client
client = bybit.bybit(test=False, api_key=os.environ.get("BYBIT_API_KEY"), api_secret=os.environ.get("BYBIT_API_SECRET"))

# Define the Bybit API endpoint
SYMBOL = "1000PEPEUSDT"
API_ENDPOINT = f"https://api.bybit.com/v2/public/tickers?symbol={SYMBOL}"

# Create the Telegram bot
bot = telegram.Bot(token=TOKEN)

async def send_price():
    while True:
        try:
            # Retrieve the price from Bybit
            response = requests.get(API_ENDPOINT)
            data = response.json()
            price = data["result"][0]["last_price"]
            
            # Send the price to the Telegram channel
            message = f"PEPE Perpetual Contract Price: {price:.2f} USDT"
            await bot.send_message(chat_id=CHAT_ID, text=message)
            
        except Exception as e:
            print(f"Error: {e}")
        
        # Wait for 5 seconds before sending the next message
        await asyncio.sleep(5)

asyncio.run(send_price())
