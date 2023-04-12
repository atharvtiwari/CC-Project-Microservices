from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = '080_087_092_111'

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
        result =  requests.get(f"http://subtraction:5052/sub/{str(number_1)}/{str(number_2)}").text
    elif operation == 'multiply':
        result =  requests.get(f"http://multiplication:5053/mul/{str(number_1)}/{str(number_2)}").text
    elif operation == 'divide':
        result =  requests.get(f"http://division:5054/div/{str(number_1)}/{str(number_2)}").text
    else:
        result = "undefined"

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug = True,
        port = 5050,
        host = "0.0.0.0"
    )
