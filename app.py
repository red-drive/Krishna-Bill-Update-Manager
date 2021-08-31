from flask import Flask
import logging

logging.basicConfig(filename="TestLog.log",format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def index():
    logging.info("Website Up and Running")
    return "Welcome to the world of heroku master\n/<shopname>/<transaction>/<totalamount>/<lastsale>"

@app.route("/<shopname>/<transaction>/<totalamount>/<lastsale>")
def saleupdate(shopname,transaction,totalamount,lastsale):
    print(shopname+" "+transaction+" "+totalamount+" "+lastsale)
    return "200 OK"

if __name__ == '__main__':
    app.run(debug=True)