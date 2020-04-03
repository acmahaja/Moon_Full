from flask import Flask, render_template, request, redirect, url_for

import yfinance as yf
import GoogleNews as news

import requests
from bs4 import BeautifulSoup

from datetime import datetime 
from termcolor import colored, cprint
import json
from datetime import datetime 

import pandas as pd

def share_check(stock_val):
   try:
      stock = yf.Ticker(stock_val)
   except:
      return False
   if(stock.info['symbol'] == stock_val):
        return True
   return False

def live_share_result(stock_val):
   url = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/"+stock_val+'/book'
   headers = {
      'x-rapidapi-host': "investors-exchange-iex-trading.p.rapidapi.com",
      'x-rapidapi-key': "bd07a264aemsh6a2c106dd27fc55p1cf614jsn85f08ce4e567"
      }
   response = requests.request("GET", url, headers=headers)
   stock_request_dict = json.loads(response.text)
   return str(stock_request_dict['quote']['latestPrice'])

def market_status(stock_val):
   url = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/"+stock_val+'/book'
   headers = {
      'x-rapidapi-host': "investors-exchange-iex-trading.p.rapidapi.com",
      'x-rapidapi-key': "bd07a264aemsh6a2c106dd27fc55p1cf614jsn85f08ce4e567"
      }
   response = requests.request("GET", url, headers=headers)
   stock_request_dict = json.loads(response.text)
   return str(stock_request_dict['quote']['latestSource'])

def share_result(stock_request):
   stock = yf.Ticker(stock_request['stock'])
   #print(stock.info)
   result = stock.history(period="1d")
   result_period = stock.history(period=stock_request['period'], interval= "1h")
   difference = float(live_share_result(stock_request['stock'])) - stock.info['previousClose']
   percentage_difference = difference / result['Open'][0]
   stock_result = {
      'stock':stock_request['stock'],
      'period':stock_request['period'],
      'full_name': stock.info['shortName'],
      'open': result['Open'][0],
      'change': difference,
      'percentage': round(percentage_difference,4)*100,
      'dates':result_period.index.values,
      'opening_overtime':result_period[['Open']].to_dict('list'),
      'closing_overtime':result_period[['Close']].to_dict('list'),
      'logo':stock.info['logo_url'],
      'weblink': stock.info['website']
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
            #print(stock_data['full_name'])
            return render_template('stock_view.html', 
                                       title=stock_request['stock'],
                                          stock_full_name = stock_data['full_name'],
                                             logo = stock_data['logo'],
                                                weblink = stock_data['weblink'],
                                                   current = live_share_result(str(stock_name)),
                                                      percentage = stock_data['percentage'],
                                                         market_status = market_status(str(stock_name)),
                                                            difference = round(stock_data['change'],2),
                                                                  labels=stock_data['dates'], 
                                                                     values=stock_data['closing_overtime']['Close'])


if __name__ == '__main__':
   app.run()
