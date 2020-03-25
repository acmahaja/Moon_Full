from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/stock', methods = ['POST', 'GET'])
def stock():
      if request.method == 'POST':
         result = request.form
         return result
 
if __name__ == '__main__':
   app.run()
