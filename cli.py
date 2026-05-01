import typer
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price
)
from bot.logging_config import setup_logging

app = typer.Typer()

@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., help="MARKET, LIMIT, STOP"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT/STOP)"),
    stop_price: float = typer.Option(None, help="Stop price (required for STOP)")
    
):
    """
    Place an order on Binance Futures Testnet
    """

    setup_logging()

    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)
        validate_stop_price(order_type, stop_price)

        client = BinanceClient()
        service = OrderService(client)

        print("\n📌 Order Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        if stop_price:
            print(f"Stop Price: {stop_price}")

        response = service.place_order(
            symbol, side, order_type, quantity, price, stop_price
        )

        print("\n📊 Response:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order executed successfully")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    app()