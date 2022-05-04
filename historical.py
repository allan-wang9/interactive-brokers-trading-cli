# Author: Allan Wang 
# TICKER HISTORICAL DATA QUERY
# Retrieves the historical data of a specified ticker.
# IB-insync is a Python library that is used with TWS API to allow us to make cool trading programs!

#----------------------------------------------------------------------------------------------------

# Import the library and declare "ib" instance
from ib_insync import *
ib = IB()

# Uncomment below to use IB Gateway Portal
# ib.connect('127.0.0.1', 7497, clientId=1)

# Connect via TWS (Trader Workstation)
# Client ID = # of logged users 
ib.connect('127.0.0.1', 7497, clientId = 1)

#----------------------------------------------------------------------------------------------------
# INPUT DESIRED TICKER INFORMATION BELOW

ticker_selection = input("Enter a ticker to view historical data (or 'quit' to exit): ")

while ticker_selection != quit:

    if ticker_selection == "quit":
        print("Goodbye!")
        exit()

    TICKER = ticker_selection
    EXCHANGE = 'SMART'    #auto-detect exchange
    CURRENCY = 'USD'      #currency to display

    # Initialize new stock information above
    stock = Stock(TICKER, EXCHANGE, CURRENCY)

    # Get historical bar data  
    bars = ib.reqHistoricalData(stock, 
        endDateTime = '', durationStr = '30 D', 
        barSizeSetting = '1 hour', whatToShow = 'MIDPOINT', useRTH = True)

    # Convert to pandas dataframe (terminal visualizer) 
    dataframe = util.df(bars)
    print("Distorical data for ticker: " + TICKER + "\n")
    print(dataframe)

    ticker_selection = input("Enter a ticker to view historical data (or 'quit' to exit): ")

#----------------------------------------------------------------------------------------------------

# Request realtime market data by attaching callback function -> onPendingTicker
market_data = ib.reqMktData(stock, '', False, False)

def onPendingTicker(ticker):
    print("Pending ticker event is successfully received:")
    print(ticker)

#----------------------------------------------------------------------------------------------------
#ib.pendingTickersEvent += onPendingTicker
#ib.run()