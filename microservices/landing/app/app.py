from flask import Flask, render_template, request, flash

import requests
import os

app = Flask(__name__)
app.secret_key = '080_087_092_111'

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = request.form.get('first')
        if number_1 == "":
            raise ValueError("No value entered, defaults to 0.0")
    except ValueError as e:
        number_1 = 0.0
    try:
        number_2 = request.form.get('second')
        if number_2 == "":
            raise ValueError("No value entered, defaults to 0.0")
    except ValueError as e:
        number_2 = 0.0

    operation_mapping = {
        "add":  {
            "operation": "addition",
            "port": 5051,
            "method": "add",
        },
        "subtract":  {
            "operation": "subtraction",
            "port": 5052,
            "method": "sub"
        },
        "multiply":  {
            "operation": "multiplication",
            "port": 5053,
            "method": "mul"
        },
        "divide":  {
            "operation": "division",
            "port": 5054,
            "method": "div"
        },
        "gcd":  {
            "operation": "gcd",
            "port": 5055,
            "method": "gcd"
        },
        "lcm":  {
            "operation": "lcm",
            "port": 5056,
            "method": "lcm"
        },
        "mod":  {
            "operation": "modulus",
            "port": 5057,
            "method": "mod"
        },
        "exp":  {
            "operation": "exponent",
            "port": 5058,
            "method": "exp"
        },
        "gt":  {
            "operation": "greater_than",
            "port": 5059,
            "method": "gt"
        },
        "lt":  {
            "operation": "less_than",
            "port": 5060,
            "method": "lt"
        },
        "eq":  {
            "operation": "equal",
            "port": 5061,
            "method": "eq"
        },
        "sin": {
            "operation": "sine",
            "port": 5062,
            "method": "sin"
        },
        "cos": {
            "operation": "cosine",
            "port": 5063,
            "method": "cos"
        }
    }

    operation = request.form.get('operation')

    try:
        op = operation_mapping[operation]
        result = requests.get(f"http://{op['operation']}:{op['port']}/{op['method']}/{str(float(number_1))}/{str(float(number_2))}").json()

        if result["error"]:
            raise TypeError(result["message"])
        
        if op['operation'] in ['cosine', 'sine']:
            flash(f"The result of operation {operation} on {float(number_1)} degree(s) is {result['result']}")
        else:
            flash(f"The result of operation {operation} on {float(number_1)} and {float(number_2)} is {result['result']}")
    except (ValueError, TypeError) as e:
        flash(e)
    except:
        flash(f"Please select an operation")

    return render_template('index.html', choices=operation_mapping)

if __name__ == '__main__':
    app.run(
        debug = True,
        port = 5050,
        host = "0.0.0.0"
    )
