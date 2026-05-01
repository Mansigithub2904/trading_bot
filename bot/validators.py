def validate_symbol(symbol: str):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g., BTCUSDT)")

def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

def validate_price(order_type: str, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

def validate_stop_price(order_type: str, stop_price):
    if order_type == "STOP" and stop_price is None:
        raise ValueError("stop_price is required for STOP orders")