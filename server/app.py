#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string_to_print>')
def print_string(string_to_print):
    print(string_to_print)
    return f'Printed string: {string_to_print}'

@app.route('/count/<int:number_to_count>')
def count(number_to_count):
    numbers = '\n'.join(str(x) for x in range(number_to_count))
    return f'Counted numbers:\n{numbers}'

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Cannot divide by zero!'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return 'Cannot modulo by zero!'
    else:
        return 'Invalid operation! Supported operations: +, -, *, div, %'

    return f'Result of {num1} {operation} {num2} is: {result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
