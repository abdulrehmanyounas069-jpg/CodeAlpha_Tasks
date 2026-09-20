# Stock Portfolio Tracker
# CodeAlpha Python Internship - Task 2

# Hardcoded stock prices (like the task instructions say)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}
def get_portfolio():
    portfolio = {}

    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    print("\nEnter stock name and quantity. Type 'done' when finished.\n")

    while True:
        stock = input("Stock name (or 'done'): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("That stock is not in the list, try again.")
            continue

        qty = input(f"Quantity of {stock}: ").strip()

        if not qty.isdigit():
            print("Please enter a valid whole number for quantity.")
            continue

        qty = int(qty)
        portfolio[stock] = portfolio.get(stock, 0) + qty

    return portfolio


def calculate_total(portfolio):
    total = 0
    for stock, qty in portfolio.items():
        total += stock_prices[stock] * qty
    return total


def show_summary(portfolio, total):
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        cost = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${cost}")
    print(f"Total investment: ${total}")


def save_to_file(portfolio, total):
    save = input("\nSave this summary to a file? (y/n): ").lower().strip()

    if save != "y":
        return

    with open("portfolio_summary.txt", "w") as f:
        f.write("Portfolio Summary\n")
        f.write("------------------\n")
        for stock, qty in portfolio.items():
            cost = stock_prices[stock] * qty
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${cost}\n")
        f.write(f"Total investment: ${total}\n")

    print("Saved to portfolio_summary.txt")


def main():
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = calculate_total(portfolio)
    show_summary(portfolio, total)
    save_to_file(portfolio, total)


if __name__ == "__main__":
    main()