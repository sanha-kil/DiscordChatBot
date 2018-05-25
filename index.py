from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import pymysql
from pymysql.cursors import DictCursor

app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='root',
    database='wapvote',
    password='k@950629',
    charset='utf8'
)

cursor = conn.cursor(DictCursor)

@app.route("/")
@app.route("/home")
@app.route("/onsurvey")
def home():
    return render_template('onsurvey.html')

@app.route("/endsurvey")
def endsurvey():
    return render_template('endsurvey.html')

@app.route("/makesurvey", methods = ['GET','POST'])
def makesurvey():
    error = None
    return render_template('makesurvey.html')

@app.route("/tae")
def tae():
    return render_template('tae.html')

if __name__ == "__main__":
    app.run(debug = True, port = 80)