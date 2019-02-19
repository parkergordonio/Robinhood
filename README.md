# Robinhood

[![Join the chat at https://gitter.im/J-Robinhood/Lobby](https://badges.gitter.im/J-Robinhood/Lobby.svg)](https://gitter.im/J-Robinhood/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Python Framework to make trades with Robinhood Private API.
See this [blog post](https://medium.com/@rohanpai25/reversing-robinhood-free-accessible-automated-stock-trading-f40fba1e7d8b).

## Current Features 
- Placing buy orders (`Robinhood.place_buy_order`)
- Placing sell order (`Robinhood.place_sell_order`)
- Fetch and cancel orders (`Robinhood.order_history` and `Robinhood.cancel_order`)
- Quote information (`Robinhood.quote_data`)
- User portfolio data (`Robinhood.portfolios`)
- User positions data (`Robinhood.positions`)
- More coming soon

### How To Install:
#### Install Python Modules
    pip install .
    
#### Add Robinhood Password Env Variable
Exit your ~/.bash_profile to export your Robinhood password like:
```export xcFrd="THIS_IS_YOUR_PASS"```

"xcFrd" is something made up, but provides a bit of obfuscation in the event that someone has access to your terminal when you're not looking. Using "Robinhood_password" would give the attacker enough context to know what to do with it.

### Converting to Python 3
Project will work on both python 2 and python 3

### How to Use (see [example.py](https://github.com/Jamonek/Robinhood/blob/master/docs/example.py))

    from Robinhood import Robinhood
    my_trader = Robinhood()
    logged_in = my_trader.login(username="USERNAME HERE", password="PASSWORD HERE")
    stock_instrument = my_trader.instruments("GEVO")[0]
    quote_info = my_trader.quote_data("GEVO")
    buy_order = my_trader.place_buy_order(stock_instrument, 1)
    sell_order = my_trader.place_sell_order(stock_instrument, 1)

### Data returned
* Quote data
  + Ask Price
  + Ask Size
  + Bid Price
  + Bid Size
  + Last trade price
  + Previous close
  + Previous close date
  + Adjusted previous close
  + Trading halted
  + Updated at
  + Historical Price
* User portfolio data
  + Adjusted equity previous close
  + Equity
  + Equity previous close
  + Excess margin
  + Extended hours equity
  + Extended hours market value
  + Last core equity
  + Last core market value
  + Market value
  + Order history
  + Dividend history
* User positions data
  + Securities owned
* News

------------------

# Related

* [robinhood-ruby](https://github.com/rememberlenny/robinhood-ruby) - RubyGem for interacting with Robinhood API
* [robinhood-node](https://github.com/aurbano/robinhood-node) - NodeJS module to make trades with Robinhood Private API
