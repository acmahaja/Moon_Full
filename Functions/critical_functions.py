import yfinance
import GoogleNews as news
from datetime import datetime 
from termcolor import colored, cprint
import string


def share_about(stock_val):
    sol = yfinance.Ticker(stock_val)
    sol_dict = sol.get_info()
    cprint(sol_dict['shortName'],'green')
    cprint(sol_dict['sector'], 'green')
    cprint(sol_dict['address1'], 'green')
    cprint(sol_dict['city'], 'green')
    cprint(sol_dict['state'], 'green')
    cprint(sol_dict['country'], 'green')


def share_value(stock_val):
    sol = yfinance.Ticker(stock_val)
    sol_day = sol.history(period="1d")
    sol_opening = sol_day['Open']
    print(sol_opening)
    sol_current = sol_day['Close']
    print(sol_current)
    difference = sol_current - sol_opening
    print(difference)

def share(stock_val):
    share_about(stock_val)
    share_value(stock_val)

def share_check(stock_val):
    sol = yfinance.Ticker(stock_val)
    try:
        info = sol.get_info()
    except:
        return False
    
    if(info['shortName']):
        return True
    return False

def main():
    cprint("Welcome to Stock Trader", 'green')
    while(True):
        cprint("Ctrl+C to exit or Enter \'exit\'", 'yellow')
        try:
            stock =  input("Enter Stock\n")
            stock = stock.upper()
            if(stock == 'exit'):
                cprint("Exiting", 'yellow')
                break
            elif(stock != 'exit'):
                if not stock:
                    cprint("Missing Value", 'red')
                else:
                    if not share_check(stock):
                        cprint("Error " + stock + " not found", 'red')
                    else:
                        cprint("Stock exists", 'green')
                        share(stock)

        except KeyboardInterrupt:
            cprint("Exiting", 'yellow')
            break

if __name__ == "__main__":
    # execute only if run as a script
    run = True
    main()
