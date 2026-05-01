# Binance Futures Testnet Trading Bot

## Setup

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create `.env` file:
   BINANCE_API_KEY=your_key
   BINANCE_API_SECRET=your_secret

## Run Examples

### Market Order
python cli.py trade --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01

### Limit Order
python cli.py trade --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 65000

### Stop-Limit Order (Bonus)
python cli.py trade --symbol BTCUSDT --side BUY --order-type STOP --quantity 0.01 --price 65000 --stop-price 64500

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