import requests

# Replace 'YOUR_API_KEY' with your actual ExchangeRate-API key
API_KEY = 'fca_live_3SJypqaMnnilmbicuVZZcX9SXndF7we8Lq6bmOsC'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

def get_exchange_rates():
    response = requests.get(f'{BASE_URL}/{API_KEY}/latest/USD')
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Unable to fetch exchange rates.")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount_in_usd = amount / rates[from_currency]
    else:
        amount_in_usd = amount

    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

def main():
    exchange_rates = get_exchange_rates()
    if not exchange_rates:
        return

    rates = exchange_rates['conversion_rates']
    currencies = list(rates.keys())

    print("Available currencies:", ", ".join(currencies))

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print("Error: Invalid currency code.")
        return

    converted_amount = convert_currency(amount, from_currency, to_currency, rates)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
