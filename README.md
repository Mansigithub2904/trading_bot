# Binance Futures Testnet Trading Bot

## Setup

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create `.env` file:
   BINANCE_API_KEY=your_key
   BINANCE_API_SECRET=your_secret

4. Ensure you are using Binance Futures Testnet API keys.

## Run Examples

### Market Order
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 80000

## Note on STOP Orders
Binance Futures Testnet has limited support for STOP / STOP_MARKET orders via standard endpoints.
To demonstrate functionality, STOP orders are implemented and validated, but simulated during execution.
MARKET and LIMIT orders are fully functional and tested against the testnet API.

## Features

- Market, Limit, and Stop-Limit orders
- BUY / SELL support
- CLI input validation
- Structured architecture
- Logging (requests, responses, errors)
- Exception handling

## Logs

Check logs/app.log for execution details.

## Assumptions

- Only USDT-M Futures supported
- Binance Testnet used