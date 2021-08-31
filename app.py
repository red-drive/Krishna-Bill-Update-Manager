from flask import Flask,render_template
import logging

logging.basicConfig(filename="TestLog.log",format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
app = Flask(__name__)

@app.route("/")
def index():
    logging.info("Website Up and Running")
    return render_template("index.html")

@app.route("/<shopname>/<transaction>/<totalamount>/<lastsale>",methods=["POST"])
def saleupdate(shopname,transaction,totalamount,lastsale):
    print(shopname+" "+transaction+" "+totalamount+" "+lastsale)
    return "200 OK"

if __name__ == '__main__':
    app.run(debug=True)