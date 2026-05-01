# 🚀 Binance Futures Testnet Trading Bot

A clean, modular Python CLI application to place **MARKET** and **LIMIT** orders on Binance Futures Testnet, with robust validation, logging, and error handling.

---

## 📌 Overview

This project demonstrates a production-style architecture for interacting with trading APIs. It focuses on:

* Clean code structure
* Input validation
* Reliable API interaction
* Logging and error handling

---

## ✨ Features

* ✅ Place **MARKET orders**
* ✅ Place **LIMIT orders**
* ⚠️ Support for **STOP orders (simulated)** due to Binance Testnet limitations
* ✅ BUY / SELL support
* ✅ CLI-based interaction (using Typer)
* ✅ Input validation layer
* ✅ Structured logging (requests, responses, errors)

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance API wrapper
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
├── .env                 # API credentials (not committed)
└── logs/
```

---

## ⚙️ Requirements

* Python 3.10+
* Binance Futures Testnet account
* Testnet API Key & Secret

---

## 🔐 Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

> ⚠️ Use **Binance Futures Testnet** keys only

---

## ▶️ Usage

### 📈 Market Order

```
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

---

### 📊 Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 80000
```

---

### ⚠️ Stop Order (Simulated)

```
python cli.py --symbol BTCUSDT --side BUY --order-type STOP --quantity 0.01 --stop-price 79000
```

> Note: STOP orders are simulated due to limited support in Binance Futures Testnet API.

---

## 📊 Sample Output

```
📌 Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

📊 Response:
Order ID: 123456
Status: FILLED
Executed Qty: 0.01
Avg Price: 65000

✅ Order executed successfully
```

---

## 📝 Logging

Logs are stored in:

```
logs/app.log
```

Example log:

```
INFO - Sending order request: {...}
INFO - Received response: {...}
ERROR - API Error: insufficient balance
```

---

## ⚠️ Important Notes

* Only **USDT-M Futures** supported
* Testnet environment may not support all order types
* STOP orders are implemented for structure but simulated

---

## 🔒 Security

* API keys are stored in `.env`
* `.env` is excluded via `.gitignore`
* Never expose credentials publicly

---

## 🧠 Design Highlights

* Separation of concerns (API / logic / validation / CLI)
* Scalable structure for adding new order types
* Defensive programming via validation and exception handling
* Real-world API interaction with logging

---

## 🚀 Future Improvements

* Add support for OCO / advanced orders
* Precision handling (tick size, lot size)
* Retry mechanism for API failures
* Web UI or dashboard

---

## 👤 Author

Mansi Patil

---

## 📄 License

This project is for educational and demonstration purposes.
