from flask import Flask, render_template, request, redirect, url_for

import yfinance as yf
import GoogleNews as news

from datetime import datetime 
from termcolor import colored, cprint
from datetime import datetime 

import pandas as pd

def share_check(stock_val):
   try:
      stock = yf.Ticker(stock_val)
   except:
      return False

   if(stock is not None):
        return True
   return False


def share_result(stock_request):
#   stock = yf.Ticker(string(stock_request['stock']))
#   stock_day = stock.history(period="max")
   stock = yf.Ticker(stock_request['stock'])
   result = stock.history(period="1d")
   result_period = stock.history(period=stock_request['period'])
   difference = result['Open'][0] - result['Close'][0]
   stock_result = {
      'stock':stock_request['stock'],
      'period':stock_request['period'],
      'open': result['Open'][0],
      'current': result['Close'][0],
      'change': difference,
      'dates':result_period.index.values,
      'Opening_overtime':result_period[['Open']].to_dict('list'),
      'Closing_overtime':result_period[['Close']].to_dict('list')
   }

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
            stock_data = share_result(stock_request)
            val = stock_data['dates']
            return render_template('stock_view.html', result = stock_data)


if __name__ == '__main__':
   app.run()
