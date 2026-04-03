import argparse
from bot.client import BinanceClient
from bot.validators import validate_side, validate_order_type
from bot.orders import format_order_response
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT)")
    args = parser.parse_args()

    # Setup logging
    setup_logger("binance")

    # Validate inputs
    side = validate_side(args.side.upper())
    order_type = validate_order_type(args.type.upper())

    # Initialize client (replace with your testnet API keys)
    api_key = "YOUR_TESTNET_API_KEY"
    api_secret = "YOUR_TESTNET_API_SECRET"
    client = BinanceClient(api_key, api_secret)

    try:
        order = client.place_order(
            symbol=args.symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=args.quantity,
            price=args.price
        )
        response = format_order_response(order)
        print("✅ Order placed successfully!")
        print(response)
    except Exception as e:
        print(f"Failed to place order: {e}")

if __name__ == "__main__":
    main()
