from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_name():
 return 'Hello'

@app.route('/<name>')
def hello(name):
 return 'Hello ' + name + '!!'

# @app.route('/shah')
# def hello_shah():
#  return 'Hello shah'

# @app.route('/')
# def hello_yawar():
#  return 'Hello yawar'
if __name__ == '__main__':
     app.run()