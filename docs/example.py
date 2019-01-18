from Robinhood import Robinhood
import os

# Password
robin_pass = os.environ['xcFrd']

#Setup
my_trader = Robinhood()

#login
try:
    my_trader.login(username="pgaasu@gmail.com", password=robin_pass)
except:
    print "Could not login. Need 2FA code...."
    multiFA = input("2FA Code? ")
    my_trader.login(username="pgaasu@gmail.com", password=robin_pass, mfa_code=multiFA)
    print "...Logged in"

#Get stock information
    #Note: Sometimes more than one instrument may be returned for a given stock symbol
# stock_instrument = my_trader.instruments("GEVO")[0]
print(my_trader.positions())

port = my_trader.portfolios()
print(port)

#Get a stock's quote
# my_trader.print_quote("GE")

# my_trader.print_quote()

# #Print multiple symbols
# my_trader.print_quotes(stocks=["BBRY", "FB", "MSFT"])

# #View all data for a given stock ie. Ask price and size, bid price and size, previous close, adjusted previous close, etc.
# quote_info = my_trader.quote_data("GE")
# print(quote_info)

# #Place a buy order (uses market bid price)
# buy_order = my_trader.place_buy_order(stock_instrument, 1)

# #Place a sell order
# sell_order = my_trader.place_sell_order(stock_instrument, 1)
