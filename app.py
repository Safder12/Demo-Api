from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_name():
    return 'Hello'

@app.route('/<name>')
def hello(name):
    return 'Hello ' + name + '!!'

if __name__ == '__main__':
    app.run()
