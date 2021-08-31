from flask import Flask
import logging

logging.basicConfig(filename="TestLog.log",format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def index():
    logging.info("Website Up and Running")
    return "Welcome to the world of heroku master"


if __name__ == '__main__':
    app.run(debug=True)