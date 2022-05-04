# Author: Allan Wang 
# PLACE ORDERS 
# Open or add to a new position.
# IB-insync is a Python library that is used with TWS API to allow us to make cool trading programs!

#----------------------------------------------------------------------------------------------------

# Import the library, declare "ib" instance and connect via TWS
from ib_insync import *
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

#----------------------------------------------------------------------------------------------------

'''
1. Enter the ticker symbol you want to buy.
2. Enter the exchange to buy from. Use "SMART" to auto-find the most popular exchange for the ticker.
3. Enter the currency (should be the same as the funds in your IBKR account.)  
'''

ticker_selection = input("Enter a stock ticker to buy quit(or 'quit' to exit): ")

while ticker_selection != quit:

    if ticker_selection == "quit":
        print("Goodbye!")
        exit()

    TICKER   = ticker_selection
    EXCHANGE = 'SMART'    #auto-detect exchange
    CURRENCY = 'USD'      #currency to display

    stock = Stock(TICKER, EXCHANGE, CURRENCY)

    '''
    4. Select the quantity you wish to buy.
    5. Select the appropriate order type.
    '''

    # Select type of market order here:

    print("Select an order type:")
    print("1 - Market Order")
    print("2 - Limit Order")
    user_selection = input("Enter your order type:")

    if user_selection == "1":
        quantity = input("Enter the quantity: ")
        order = MarketOrder('BUY', quantity)

    elif user_selection == "2":
        quantity = input("Enter the quantity: ")
        limit_price = input("Enter the limit price: ")
        order = LimitOrder('BUY', quantity, limit_price)

    else:
        print("Please enter a valid order type.")
        quit()


    #Fill the order and print the confirmation the client
    trade = ib.placeOrder(stock, order)
    print(trade)

    ticker_selection = input("Enter a stock ticker to buy(or 'quit' to exit): ")

#----------------------------------------------------------------------------------------------------
#Display order fill details upon order completion

def orderFilled(trade, fill):
    print("Order Filled!")
    print(trade)
    print(fill)

trade.fillEvent += orderFilled
ib.sleep(3)

#----------------------------------------------------------------------------------------------------
#Display recent trades and orders 

print("List of trades made (sorted by day):\n")
for trades in ib.trades():
    print("Trade Details:")
    print(trades)

print("\n")

print("Order History:\n")
for orders in ib.orders():
    print("Orders:")
    print(orders)

#----------------------------------------------------------------------------------------------------
ib.run()