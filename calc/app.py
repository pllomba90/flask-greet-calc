# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a,b)

    return str(sum)

@app.route('/sub')
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    difference = sub(a,b)

    return str(difference)

@app.route('/mult')
def product():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = mult(a,b)

    return str(total)

@app.route('/div')
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    quotient = div(a,b)

    return str(quotient)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
