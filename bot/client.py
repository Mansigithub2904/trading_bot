from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found in .env file")

        self.client = Client(self.api_key, self.api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)