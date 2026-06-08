print("-----Welcome to Stock Portfolio Tracker-----")
print("1. Enter the number of stocks")
print("2. Enter stock names")
print("3. Enter quantity for each stock")
print("4. Get the total investment value")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

total_investment = 0
portfolio = {}

num_stocks = int(input("How many stocks do you want to add? "))

for i in range(num_stocks):

    print(f"Stock {i + 1}")

    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        portfolio[stock_name] = quantity

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not available")

print("-----Portfolio Summary-----")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    print(stock, " Quantity:", quantity,
          ", Price: $", price,
          ", Total: $", investment)

print("Total Investment Value: $", total_investment)