import csv

# function 1 - read portfolios into dictionary
def read_portfolios_csv(file):
    portfolios = {}
    with open(file, 'r') as file:
        reader = csv.reader(file)
        current_portfolio = None
        shares = {}

        for row in reader:
            if row[0] == "NAME":
                continue
            if row[1] == '':
                if current_portfolio is not None:
                    portfolios[current_portfolio] = resolve_nested_portfolios(shares, portfolios)
                    shares = {}
                current_portfolio = row[0]
            else:
                shares[row[0]] = int(row[1])

        if current_portfolio is not None:
            portfolios[current_portfolio] = resolve_nested_portfolios(shares, portfolios)

    return portfolios

def resolve_nested_portfolios(shares, portfolios):
    resolved_shares = {}
    for stock, quantity in shares.items():
        nested_portfolio = portfolios.get(stock)
        if nested_portfolio:
            nested_shares = resolve_nested_portfolios(nested_portfolio, portfolios)
            for nested_stock, nested_quantity in nested_shares.items():
                resolved_shares[nested_stock] = resolved_shares.get(nested_stock, 0) + nested_quantity * quantity
        else:
            resolved_shares[stock] = quantity
    return resolved_shares

# function 2 - process stock_price_stream data & calculate portfolio prices
def calculate_portfolio_prices(portfolios, input_file, output_file):
    price_changes = {}  # dictionary to store stock price changes
    portfolio_values = {}  # track portfolio values to avoid repetition

    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        
        with open(output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(["NAME", "PRICE"])

            for row in reader:
                stock_name = row[0]
                stock_price = float(row[1])
                price_changes[stock_name] = stock_price
                print("[STOCK]", stock_name, "-->", stock_price)

                # stock price update
                writer.writerow([stock_name, stock_price])

                # update portfolio prices
                for portfolio_name, stocks in portfolios.items():
                    if all(stock in price_changes for stock in stocks):
                        # calculate portfolio value using dictionary lookup
                        value = sum(stocks[stock] * price_changes[stock] for stock in stocks)
                        if portfolio_name not in portfolio_values or portfolio_values[portfolio_name] != value:
                            # write the portfolio value only if it has changed
                            writer.writerow([portfolio_name, value])
                            portfolio_values[portfolio_name] = value
                            print("[PORTFOLIO]", portfolio_name, "-->", value)

# input/output parameters
portfolios_csv = "./inputs/portfolios.csv"
stock_price_stream = "./inputs/prices.csv"
output = "./outputs/portfolio_prices.csv"

# main program function
def main():
    portfolios = read_portfolios_csv(portfolios_csv)
    calculate_portfolio_prices(portfolios, stock_price_stream, output)
    print()
    print("updated stock prices and portfolio values outputted: ./outputs/portfolio_prices.csv")

# execute main program func when ran directly
if __name__ == "__main__":
    main()