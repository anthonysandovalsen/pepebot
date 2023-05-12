import asyncio
import logging
import os

import aiohttp
import telegram


# Replace the API key and chat ID with your own
TOKEN = "5723647924:AAEr7fodamyolFNJW7NGjqIlgjYEScmeuwY"
CHAT_ID = "1613266416"

# Define the Bybit API endpoint and parameters
API_ENDPOINT = "https://api.bybit.com/v2/public/tickers"
SYMBOL = "1000PEPEUSDT"

# Create the Telegram bot
bot = telegram.Bot(token=TOKEN)

# Set up logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def fetch_price(session):
    params = {"symbol": SYMBOL}
    async with session.get(API_ENDPOINT, params=params) as response:
        data = await response.json()
        price = float(data["result"][0]["last_price"])
        return price


async def send_price():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                price = await fetch_price(session)
                message = f"{SYMBOL} Price: {price:.2f} USDT"
                await bot.send_message(chat_id=CHAT_ID, text=message)
                logging.info("Price sent successfully")

            except Exception as e:
                logging.error(f"Error: {e}")

            await asyncio.sleep(5)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_price())
