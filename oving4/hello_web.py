from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Dette er mitt første program med Flask "


if __name__ == '__main__':
    app.run(debug=True)
