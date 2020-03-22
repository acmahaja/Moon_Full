from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/<name>')
def homepage(name):
    return 'Hello %s!'% name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
    return 'Hi I\'m a Flask 🍶 Application!'

@app.route('/python/')
def hello_python():
    return 'This Flask Application has a Python 🐍 Backend!'

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/users/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

    

@app.route('/')
def hello():
    return('Hello 😊, \nChange the url\'s address 👆')


if __name__ == '__main__':
    app.run(debug=True)
