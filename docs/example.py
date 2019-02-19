from Robinhood import Robinhood
import os
import json
import pyfiglet
import time,sys
from pyfiglet import Figlet
from threading import Thread
from time import sleep
os.system('clear')

# Robinhood password environment variable name
robin_pass_key='xcFrd'

show_loading = False
def loading_animation(arg):
    while show_loading:
        blah="\|/-\|/-"
        for l in blah:
            sys.stdout.write(l)
            sys.stdout.flush()
            sys.stdout.write('\b')
            time.sleep(0.2)


f = Figlet(font='smslant')
print f.renderText('Robinhood Performance')


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

    def return_performance(self):
        return_float = (float(100) * (float(self.current_price) * float(self.units)) / float(self.initial_investment())) - 100
        return_rounded = "{0:.2f}".format(return_float)
        return return_rounded

def json_print(j):
    print(json.dumps(j, indent=4, sort_keys=True))

def round(x):
    return "{0:.2f}".format(x)

try:
    print("Logging User In...")
    robin_pass = os.environ[robin_pass_key]
    my_trader = Robinhood()
    my_trader.login(username="pgaasu@gmail.com", password=robin_pass)
except:
    print "Could not login. Need 2FA code...."
    multiFA = input("2FA Code? ")
    my_trader.login(username="pgaasu@gmail.com", password=robin_pass, mfa_code=multiFA)
    print "...Logged in"

# Get stock information
# Note: Sometimes more than one instrument may be returned for a given stock symbol

positions = my_trader.positions()

# Start Loading Animation
show_loading = True
print("Pulling Robinhood Data...")
animation_thread = Thread(target = loading_animation, args = (10, ))
animation_thread.start()


# Initial Total Equity
all_stocks = positions['results']
owned_stocks = list(filter(lambda x: float(x['quantity']) > 0, all_stocks))

def toPerformance(i):
    instrument_link = i['instrument']
    # Get Symbol, Quote from instrument
    instrument = my_trader.instrument_from_link(instrument_link)
    quote_data = my_trader.quote_data(instrument['symbol'])

    perf = Performance()
    perf.units = i['quantity']
    perf.average_buy_price = i['average_buy_price']
    perf.symbol = instrument['symbol']
    perf.current_price = quote_data['last_trade_price']
    return perf

stock_performance = list(map(lambda x: toPerformance(x), owned_stocks))
stock_performance.sort(reverse=True, key=lambda p: float(p.return_performance()))


portfolio = my_trader.portfolios()
stockValue = portfolio['last_core_market_value']
cashValue = float(portfolio['last_core_equity']) - float(portfolio['last_core_market_value'])

# Complete the Loading Animation
show_loading = False
animation_thread.join()

print("\n\n")
print("---------------------------------")
print("|\tAccount            \t|")
print("---------------------------------")
print("| Stocks\t| $" + stockValue + "\t|")
print("| Cash  \t| $" + str(cashValue) + "\t|")
print("_________________________________")
print("\n")
print("---------------------------------")
print("|\tStock Performance \t|")
print("---------------------------------")

for p in stock_performance:
    print("| (" + p.symbol + ")  \t\t\t|")
    print("|   Invested: $(" + p.inital_investment_str() + ")  \t|")
    print("|   Value: $(" + str(float(p.current_price) * float(p.units)) + ") \t\t|")
    return_float = (float(100) * (float(p.current_price) * float(p.units)) / float(p.initial_investment())) - 100
    return_rounded = round(return_float)
    print("|   Return: (" + str(return_rounded) + ")% \t\t|")

print("_________________________________\n\n")
print("-----------------------------------------")
print("|\tReturn Metrics       \t\t|")
print("-----------------------------------------")

stockNum=1
for p in stock_performance:
    return_float = (float(100) * (float(p.current_price) * float(p.units)) / float(p.initial_investment())) - 100
    return_rounded = round(return_float)

    gain = round(float(float(p.current_price) * float(p.units)) - float(p.initial_investment()))
    print("| " + str(stockNum) + ". (" + str(return_rounded) + ")% (" + p.symbol + "), " + "Gain: $(" + str(gain) + ") \t|")
    stockNum=stockNum+1
    # print("|----------------------------------|")
print("_________________________________________\n\n")




# EXAMPLES
# ---------------------------------------

# history=my_trader.order_history()
# json_print(history)

# print("QUOTE: \n\n")
# my_trader.print_quote("GE")

# #Print multiple symbols
# my_trader.print_quotes(stocks=["BBRY", "FB", "MSFT"])

# #View all data for a given stock ie. Ask price and size, bid price and size, previous close, adjusted previous close, etc.
# quote_info = my_trader.quote_data("GE")
# print(quote_info)

# #Place a buy order (uses market bid price)
# buy_order = my_trader.place_buy_order(stock_instrument, 1)

# #Place a sell order
# sell_order = my_trader.place_sell_order(stock_instrument, 1)