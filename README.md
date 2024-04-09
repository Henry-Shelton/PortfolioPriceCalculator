# Portfolio Price Calculator

A simple program for streaming live updates of portfolio prices based on changing stock prices.

## Description

This program enables real-time tracking of portfolio values by processing two input CSV files, a portfolio database and a stock price csv. It dynamically calculates the values of affected portfolios and enriches the stock prices input stream with the new portfolio prices.

Inputs:

* "portfolios.csv": Contains information on starting portfolios, such as the names of portfolios and the corresponding number of shares held for each stock within each portfolio.
* "prices.csv": Contains updates of stock prices, can be streamed realtime into the program.

Outputs:

* "portfolio_prices.csv": Output file containing the steam of stock price data alongside changes in portfolios (all stock constituents within a portfolio must have changed for the portfolio to update).

## Quick Start

### Dependencies

Minimum requirements: 
* Python 3.7 or later
* Operating System: Any (Windows, macOS, Linux)

### Installing

To get started, download the repository files. If you're unfamiliar with this process, you can find detailed instructions [here](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).

### Executing program

By default the input data (portfolio.csv and prices.csv) should be populated with sample data, however, this can be modified following the correct formatting or by using the data generation scripts.

1. Open your favorite Python compiler (We recommend using VSCode).

2. Run the following script:

    ```bash
    portfolio_price_calculator.py
    ```

This script will compute the changes in stock prices and their impact on portfolio values.

The individual changes in stock values are calculated using the formula: `(old_price * new_price)`. When a portfolio's value changes, it combines all constituent stock price changes `(changed_stock_1 + changed_stock_2 ...)`.

[**NOTE**: The new value of a portfolio is calculated only when there is enough stock price data to satisfy all the constituents within the portfolio, that is, all individual stocks within a portfolio have changed value. This logic works the same for updating the CUSTOM_ETF portfolios also, except all child portfolios must have undergone a change for the parent ETF value to change.]

## Generating random portfolios and price changes

Scripts to generate randomised portfolios and stock price data can be found in the generate_random_data folder.

Defaults can also be restored using the restore_defaults.py script.

## Help

Message me regarding issues or for general queries!


## Authors

[Henry Shelton](https://github.com/Henry-Shelton)


## Version History

* 0.1 (08/04/2024)
    * Initial Release


## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgments

* BoA
