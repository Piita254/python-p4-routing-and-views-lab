from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp_body = 'Python Operations with Flask Routing and Views'
    resp_status = 200
    resp = make_response(resp_body, resp_status)
    return resp

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the parameter to the console
    return parameter  # Display the parameter in the web browser

@app.route('/count/parameter/<int:number>')
def count(number):
    # Create a plain-text string with all numbers from 0 to 'number' on separate lines
    output = '\n'.join(str(i) for i in range(number + 1))
    return output  # Return as plain text

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the operation based on the operation parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation. Supported operations: +, -, *, div, %."
    
    return str(result)  # Return the result as plain text

if __name__ == '__main__':
    app.run(port=5555, debug=True)
