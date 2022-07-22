from io import BytesIO
from flask import Flask,render_template,send_file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pymysql

app = Flask(__name__,static_folder='static',template_folder='templates')

lr = LinearRegression() 
data = pd.read_csv(
        'https://raw.githubusercontent.com/dron512/javapython/main/pycharm_work/mldl/chap3/chap3.csv')
length = data['length'].to_numpy().reshape(-1,1)
weight = data['weight'].to_numpy()
lr.fit(length,weight)

@app.route("/")
def index():
    aa = "aaa 입니다"
    return render_template("index.html",key1=aa)

@app.route("/insert")
def insert():
    con = pymysql.connect(host="localhost",user="root",passwd="1234",database="test",charset="utf8")
    cur = con.cursor()

    cur.execute("insert into fish (name,length,weight) values ('bream',45,650);")
    con.commit()
    con.close()
    return "aa"

@app.route("/img/<int:aa>")
def imgdown(aa):
    img = BytesIO()
    plt.scatter(length,weight)
    plt.scatter(int(aa),lr.predict( [[int(aa)]] ))
    plt.savefig(img,format="png",dpi=100)
    plt.close()
    img.seek(0)
    return send_file(img,mimetype="image/png")


app.run(debug=True)