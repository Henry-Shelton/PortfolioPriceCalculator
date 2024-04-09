import csv
import random

def is_portfolio_row(row):
    return row['SHARES'] and not row['NAME'].endswith(',')

def ignore_portfolio_row(row):
    portfolios_to_ignore = ['CUSTOM_ETF_1', 'CUSTOM_ETF_2', 'Finance', 'Automobiles', 'Healthcare', 'Retail', 'Technology']
    return row['NAME'] not in portfolios_to_ignore

def generate_price_changes(portfolio_file, price_file):
    # read the ./inputs/portfolio.csv file to get existing stocks
    stocks = []
    with open(portfolio_file, 'r') as portfolio_csvfile:
        portfolio_reader = csv.DictReader(portfolio_csvfile)
        for row in portfolio_reader:
            if is_portfolio_row(row) and ignore_portfolio_row(row):  
                stocks.append(row['NAME'])

    # at least 10 stocks
    num_stocks = len(stocks)
    num_rows = max(10, random.randint(10, num_stocks))

    # randomly select a subset of stocks with no dupes
    selected_stocks = random.sample(stocks, k=min(num_rows, len(stocks))) 

    # random integer values for each stock
    prices = {stock: random.randint(1, 100) for stock in selected_stocks}

    with open(price_file, 'w', newline='') as price_csvfile:
        writer = csv.writer(price_csvfile)
        writer.writerow(['NAME', 'VALUE'])
        for stock in selected_stocks:
            writer.writerow([stock, prices[stock]])

if __name__ == "__main__":
    generate_price_changes('./inputs/portfolios.csv', './inputs/prices.csv')
    print("stock prices updated.")

