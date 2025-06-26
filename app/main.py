# We are creating an web application 

from flask import Flask, session
from app.test import Animal

app = Flask(__name__)

variable1 = ""

@app.route("/test", methods = ['GET'])
def my_first_web_app():
    animal = Animal()
    global variable1
    variable1 = "Hello World"
    return animal.eat() 

# Take stock code from user
@app.route("/stock/<stock_name>", methods = ["GET"])
def stock(stock_name):
    print(f"User gave stock {stock_name}")
    global variable1
    variable1 = "Hello World from stock"
    print(variable1)
    return "Hi You gave the following stock Name: " + stock_name


if __name__ == "__main__":
    app.run()
