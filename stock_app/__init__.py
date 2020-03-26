from flask import Flask, render_template, request, redirect, url_for
import yfinance
import GoogleNews as news
from datetime import datetime 
from termcolor import colored, cprint
from datetime import datetime 
import pandas as pd
from 

def share_check(stock_val):
    sol = yfinance.Ticker(stock_val)
    try:
        info = sol.get_info()
    except:
        return False
    
    if(info['shortName']):
        return True
    return False

def share_value(stock_request):
   print(stock_request)
   sol = yfinance.Ticker(str(stock_request['stock']))
   sol_day = sol.history(period = '1d')
   ser_open = pd.Series(sol_day['Open'])
   data_open = ser_open.head(2)
   open_value_open = float(data_open[0])

   ser_close = pd.Series(sol_day['Close'])
   data_close = ser_close.head(2)
   open_value_close = float(data_close[0])
   
   

   data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

   print data

   stock_result = {'open':open_value_open,'close':open_value_close,'day_change':open_value_open-open_value_close}
   return stock_result
   
   
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/stock', methods = ['POST', 'GET'])
def stock():
      if request.method == 'POST':
         stock_request = request.form.to_dict()
         stock_name = stock_request['stock']

         if(share_check(str(stock_name)) == False):
            return redirect(url_for('home'))
         else:
            stock = share_value(stock_request)
            stock_request.update(stock)
            return stock_request
            #return render_template('stock_view.html', result = share_value(stock_request))
 
if __name__ == '__main__':
   app.run()
