import csv

# default data
portfolio_data = [
    ["NAME", "SHARES"],
    ["TECH", ""],
    ["AAPL", 100],
    ["MSFT", 200],
    ["NVDA", 300],
    ["AUTOS", ""],
    ["FORD", 100],
    ["TSLA", 200],
    ["BMW", 200],
    ["INDUSTRIALS", ""],
    ["TECH", 2],
    ["AUTOS", 3]
]

prices_data = [
    ["NAME", "PRICE"],
    ["AAPL", 173],
    ["MSFT", 425],
    ["NVDA", 880],
    ["AAPL", 174]
]

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    portfolio_filename = './inputs/portfolios.csv'
    prices_filename = './inputs/prices.csv'

    write_csv(portfolio_filename, portfolio_data)
    write_csv(prices_filename, prices_data)

if __name__ == "__main__":
    main()
    print("default data restored.")