from io import BytesIO
from flask import Flask,render_template,send_file
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/boardlist")
def boardlist():
    return render_template("board/list.html")

'''
fish class
'''
@app.route("/fishcls")
def fishcls():
    data = pd.read_csv('./static/data/fish_data.csv')
    fish_input = data[['Weight','Length','Diagonal','Height','Width','Species']].to_numpy()
    fish_target = data['Species'].to_numpy()
    fish_target = np.unique(fish_target)
    return render_template("ml/fishcls.html",fish_input=fish_input,fish_target=fish_target)

'''
fish reg
'''
@app.route("/fishreg")
def fishreg():
    data = pd.read_csv('./static/data/perch_data.csv')
    print(data.head())
    fish_input = data[['length','height','width','weight']].to_numpy()
    return render_template("ml/fishreg.html",fish_input=fish_input)


@app.route("/img")
def imgdown():
    data = pd.read_excel('data.xlsx')
    legnth = data["length"].to_numpy()
    weight = data["weight"].to_numpy()
    x,y = np.random.randint(1,100,2)
    plt.scatter(legnth,weight)
    plt.scatter(x,y)
    plt.xlabel('길이')
    plt.ylabel('무게')
    img = BytesIO()
    plt.savefig(img,format="png",dpi=200)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

app.run(debug=True)