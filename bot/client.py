from binance.client import Client
import logging

class BinanceClient:
    def __init__(self, api_key, api_secret, base_url="https://testnet.binancefuture.com"):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = base_url
        self.logger = logging.getLogger("binance")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                if not price:
                    raise ValueError("Price required for LIMIT order")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            self.logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            raise
