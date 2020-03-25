from flask import Flask, render_template, request
import yfinance
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/stock', methods = ['POST', 'GET'])
def stock():
      if request.method == 'POST':
         stock_name = request.form
         return render_template('stock_view.html', result = stock_name)
 
if __name__ == '__main__':
   app.run()
