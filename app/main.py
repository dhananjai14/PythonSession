# We are creating an web application 

from flask import Flask
from app.test import Animal


app = Flask(__name__)

@app.route("/")
def my_first_web_app():
    animal = Animal()
    return animal.eat() 

if __name__ == "__main__":
    app.run()


