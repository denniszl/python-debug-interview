from flask import Flask
app = Flask(__name__)

@app.route('/things/')
def one_thing():
    return "It is a thing."

@app.route('/things/', methods=['PUT'])
def put_thing():
    return "Thanks for the thing."

if __name__ == "__main__":
    app.run()
