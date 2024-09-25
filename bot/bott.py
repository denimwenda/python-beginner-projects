import MetaTrader5 as mt5
import numpy as np
import time

# Constants
RISK_PERCENTAGE = 0.05  # Risk 5% of equity
LOT_SIZE = 0.1  # Default lot size, can be adjusted
SYMBOL = "EURUSD"  # Change to your preferred symbol

# Initialize MT5
if not mt5.initialize():
    print("Initialization failed")
    mt5.shutdown()
    exit()

# Function to calculate the lot size based on equity and risk percentage
def calculate_lot_size(equity, risk_percentage):
    risk_amount = equity * risk_percentage
    lot_size = risk_amount / (100 * 10)  # Assuming 10 pips stop loss
    return round(lot_size, 2)  # Round to 2 decimal places

# Function to place a pending order
def place_pending_order(symbol, price, stop_loss, take_profit, buy=True):
    if buy:
        order_type = mt5.ORDER_BUY_LIMIT
    else:
        order_type = mt5.ORDER_SELL_LIMIT

    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": LOT_SIZE,
        "type": order_type,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": 10,
        "magic": 123456,
        "comment": "Fibonacci Order",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    return result

# Main trading logic
def trading_logic():
    while True:
        # Get account information
        account_info = mt5.account_info()
        equity = account_info.equity
        print(f"Account equity: {equity}")

        # Calculate lot size based on equity
        lot_size = calculate_lot_size(equity, RISK_PERCENTAGE)
        
        # Logic to determine recent highs/lows and QML area
        rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 100)
        highs = [rate.high for rate in rates]
        lows = [rate.low for rate in rates]
        
        recent_high = max(highs[-20:])  # Last 20 bars
        recent_low = min(lows[-20:])  # Last 20 bars
        qml_area = (recent_high + recent_low) / 2

        # Example of placing a pending buy order
        entry_price = qml_area + 0.0010  # Adjust according to your strategy
        stop_loss = recent_low  # Set your stop loss logic
        take_profit = entry_price + (entry_price - stop_loss) * 1.618  # Example take profit at Fibonacci extension

        result = place_pending_order(SYMBOL, entry_price, stop_loss, take_profit, buy=True)
        print(f"Placed buy order: {result}")

        time.sleep(60)  # Wait for a minute before next iteration

# Start trading logic
trading_logic()

# Shutdown MT5
mt5.shutdown()