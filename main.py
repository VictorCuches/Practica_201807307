from flask import Flask

app = Flask(__name__)

@app.route('/')

def hola():
    return 'Hola Mundo 2.0 :D'

@app.route('/uno')

def hola2():
    return 'Adios mundo 3.0 D:'