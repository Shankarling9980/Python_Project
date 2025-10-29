# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 130,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!\n")

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    name = input("Enter stock symbol (e.g., AAPL): ").upper()
    qty = int(input("Enter quantity: "))
    
    if name in stock_prices:
        cost = stock_prices[name] * qty
        portfolio[name] = cost
        total_value += cost
    else:
        print("Stock not found in our list!")

print("\nYour Portfolio Summary:")
for stock, value in portfolio.items():
    print(f"{stock} : ₹{value}")

print("\nTotal Investment Value: ₹", total_value)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, value in portfolio.items():
        file.write(f"{stock}: ₹{value}\n")
    file.write(f"\nTotal Investment Value: ₹{total_value}")