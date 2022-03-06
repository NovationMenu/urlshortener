from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from controller.urlController import UrlController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/url.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secretkey'
# app.config['SERVER_NAME'] = '2me.nu'
db = SQLAlchemy(app)

urlController = UrlController()

@app.route("/", methods=['GET', 'POST'])
def index():
    # post method creates a short for a webpage
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        return urlController.addUrl(url)
    return render_template("index.html")

@app.route("/addnewurl", methods=['GET', 'POST'])
def addnewurl():
    if request.method == 'POST':
        input_json = request.get_json()
        # url = request.form['url']
        print(input_json['url'])
        url = input_json['url']
        # return('MESSAGE DEPUIS URLSHORTENENER')
        return urlController.addNewUrl(url)
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
    return urlController.redirectUrl(id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True,host=app.config["SERVER_NAME"], port=5000)
    
