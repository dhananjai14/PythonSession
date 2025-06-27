from flask import Flask , request

app = Flask(__name__)

@app.route("/health_check",  methods = ['GET'])
def health_check():
    return "Status OK"

@app.route("/say_hello/<name>", methods = ['GET'])
def say_hello(name):
    return f"hello {name}"


@app.route("/get_user_data", methods = ["POST"])
def get_data():
    if request.method == 'POST':
        message = request.get_json()
        name = message.get("name")
        print(name)
        return name


if __name__ == "__main__":
    app.run()

