# Author: Allan Wang 
# VIEW OPTION CHAIN DATA   
# View options chain data for specified stock.
# IB-insync is a Python library that is used with TWS API to allow us to make cool trading programs!

#----------------------------------------------------------------------------------------------------

# Import the library, declare "ib" instance and connect via TWS
from ib_insync import *
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

#----------------------------------------------------------------------------------------------------

'''
1. Enter the ticker symbol you want to view options data from.
2. Enter the exchange to view from. Use "SMART" to auto-find the exchange for the ticker.
3. Enter the currency (should be the same as the settled funds in your IBKR account.)  
'''

ticker_selection = input("Enter a ticker to view options chain (or 'quit' to exit): ")

while ticker_selection != quit:

    if ticker_selection == "quit":
        print("Goodbye!")
        exit()

    TICKER = ticker_selection
    EXCHANGE = 'SMART'    #auto-detect exchange
    CURRENCY = 'USD'      #currency to display

    stock = Stock(TICKER, EXCHANGE, CURRENCY)

    # Process and qualify stocks options (some stocks do not have options available)
    ib.qualifyContracts(stock)
    ib.sleep(1)

    # Display the option chains 
    option_chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)
    print("Displaying options chains for: " + TICKER.upper() + "\n")
    print(util.df(option_chains))

    # Get ticker input 
    ticker_selection = input("Enter a ticker to view options chain (or 'quit' to exit): ")