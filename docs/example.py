from Robinhood import Robinhood
import os
import json


class Performance:
    symbol = ""
    average_buy_price = 0.00
    units = 0
    current_price = 0.00

    def initial_investment(self):
        return float(self.average_buy_price) * float(self.units)

    def inital_investment_str(self):
        inv_rounded =  "{0:.2f}".format(self.initial_investment())
        return str(inv_rounded)



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

# Get stock information
# Note: Sometimes more than one instrument may be returned for a given stock symbol
# stock_instrument = my_trader.instruments("GEVO")[0]

# print("\n\n\nPOSITION DATA \n\n\n")
positions = my_trader.positions()
# print(json.dumps(positions, indent=4, sort_keys=True))

# Initial Total Equity
all_stocks = positions['results']
owned_stocks = list(filter(lambda x: float(x['quantity']) > 0, all_stocks))

def toPerformance(i):
    instrument_link = i['instrument']
    # Get Symbol, Quote from instrument
    print("Using Instrument link: " + instrument_link)
    instrument = my_trader.instrument_from_link(instrument_link)
    quote_data = my_trader.quote_data(instrument['symbol'])
    
    perf = Performance()
    perf.units = i['quantity']
    perf.average_buy_price = i['average_buy_price']
    perf.symbol = instrument['symbol']
    perf.current_price = quote_data['last_trade_price']
    # perf.current_price = quote_data['']
    return perf

stock_performance = list(map(lambda x: toPerformance(x), owned_stocks))


#performance = list(map(lambda x: float(x['quantity']) * float(x['average_buy_price']), owned_stocks))


# print("\n\n\nPORTFOLIO DATA \n\n\n")
portfolio = my_trader.portfolios()
# print(json.dumps(portfolio, indent=4, sort_keys=True))

stockValue = portfolio['last_core_market_value']
cashValue = float(portfolio['last_core_equity']) - float(portfolio['last_core_market_value'])

print("\n\n")
print("---------------------------------")
print("|\tAccount            \t|")
print("---------------------------------")
print("| Stocks\t| $" + stockValue + "\t|")
print("| Cash  \t| $" + str(cashValue) + "\t|")
print("_________________________________")
print("\n\n")
print("---------------------------------")
print("|\tStock Performance \t|")
print("---------------------------------")

for p in stock_performance:
    print("| Symb: (" + p.symbol + ")\t\t\t|")
    print("|   Invested: $(" + p.inital_investment_str() + ")\t\t|")
    print("|   Value: $(" + str(float(p.current_price) * float(p.units)) + ") \t\t|")
    return_float = (float(100) * (float(p.current_price) * float(p.units)) / float(p.initial_investment())) - 100
    return_rounded = "{0:.2f}".format(return_float)
    print("|   Return: (" + str(return_rounded) + ")% \t\t|")
print("_________________________________\n\n")

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