import ccxt
import time
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=BOT_TOKEN)

exchange = ccxt.binance()

def check_market():
    candles = exchange.fetch_ohlcv(
        "BTC/USDT",
        timeframe="15m",
        limit=50
    )

    last = candles[-1]
    price = last[4]

    message = f"BTCUSDT check OK\nPrice: {price}"

    return message


while True:
    try:
        msg = check_market()
        bot.send_message(
            chat_id=CHAT_ID,
            text=msg
        )
        time.sleep(900)

    except Exception as e:
        print(e)
        time.sleep(60)
