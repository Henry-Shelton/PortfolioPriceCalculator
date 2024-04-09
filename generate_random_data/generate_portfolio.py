import csv
import random

# list of portfolios + some ETFs (constructed from portfolios)
portfolio_names = [
    'Technology', 'Automobiles', 'Finance', 'Healthcare', 'Retail', 'CUSTOM_ETF_1', 'CUSTOM_ETF_2'
]

# stock symbols mapped to their constituent portfolio
sector_stocks = {
    'Technology': ['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
    'Automobiles': ['F', 'GM', 'TSLA'],
    'Finance': ['JPM', 'BAC', 'GS'],
    'Healthcare': ['JNJ', 'UNH'],
    'Retail': ['WMT', 'TGT'],
    
    'CUSTOM_ETF_1': random.sample(['Technology', 'Automobiles', 'Finance', 'Healthcare', 'Retail'], 2), 
    'CUSTOM_ETF_2': random.sample(['Technology', 'Automobiles', 'Finance', 'Healthcare', 'Retail'], 2)  
}

# function to generate random 
def generate_random_data(stock_symbols, custom_etf=False):
    portfolios = []
    shares = []

    for symbol in stock_symbols:
        portfolios.append(symbol)
        if custom_etf:
            shares.append(random.randint(5, 10))  # for portfolios in CUSTOM ETFs generate 5-10 shares 
        else:
            shares.append(random.randint(10, 100))  # for stocks in portfolios generate 10-100 shares

    return portfolios, shares

# write to ./inputs/portfolio.csv
def write_to_csv(filename, portfolio_names, portfolios, shares):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['NAME', 'SHARES'])
        
        # find the CUSTOM_ETF's
        custom_etf_indices = [i for i, name in enumerate(portfolio_names) if name.startswith('CUSTOM_ETF')]
        
        # populate non-CUSTOM_ETF portfolios
        for i, name in enumerate(portfolio_names):
            if i not in custom_etf_indices:
                writer.writerow([name, ''])
                for p, s in zip(portfolios[i], shares[i]):
                    writer.writerow([p, s])
        
        # populate CUSTOM_ETF portfolios
        for i in custom_etf_indices:
            writer.writerow([portfolio_names[i], ''])
            for p, s in zip(portfolios[i], shares[i]):
                if s > 10:
                    s = min(s, 10)
                writer.writerow([p, s])

# generate random data
def generate_random_portfolio_data(filename):
    portfolios = []
    shares = []

    # randomly select up to 5 sector stocks for each selected portfolio
    for sector in portfolio_names:
        stock_symbols = sector_stocks.get(sector, [])
        if sector.startswith('CUSTOM_ETF'):
            portfolio, share = generate_random_data(stock_symbols, custom_etf=True)
        else:
            portfolio, share = generate_random_data(stock_symbols)
        portfolios.append(portfolio)
        shares.append(share)

    write_to_csv(filename, portfolio_names, portfolios, shares)

# execute main program function when ran
if __name__ == "__main__":
    generate_random_portfolio_data('./inputs/portfolios.csv')
    print("new portfolios created.")
