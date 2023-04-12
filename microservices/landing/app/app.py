from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = '080_087_092_111'

def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2 == 0:
        if n1 == 0:
            return "undefined"
        return float("inf")
    return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        float(request.form.get('first'))
        number_1 = float(request.form.get('first'))
    except:
        number_1 = 0
    try:
        float(request.form.get('second'))
        number_2 = float(request.form.get('second'))
    except:
        number_2 = 0

    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get(f'http://addition:5051/add/{str(number_1)}/{str(number_2)}').text
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
    else:
        result = "undefined"

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )