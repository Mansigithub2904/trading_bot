import logging

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params.update({
                    "price": price,
                    "timeInForce": "GTC"
                })

            elif order_type == "STOP":
                logging.warning("STOP orders not fully supported on testnet. Simulating order.")
                return {
                    "orderId": "SIMULATED_STOP_ORDER",
                    "status": "SIMULATED",
                    "executedQty": 0,
                    "avgPrice": "N/A"
                }

            logging.info(f"Sending order request: {params}")

            response = self.client.create_order(**params)

            logging.info(f"Received response: {response}")

            return response

        except Exception as e:
            logging.error(f"Order failed: {str(e)}")
            raise