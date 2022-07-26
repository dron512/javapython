from flask import Blueprint,render_template,send_file,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
from sklearn.neighbors import KNeighborsClassifier

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

ml = Blueprint("ml",__name__,url_prefix="/ml")
cls_data = pd.read_csv('./static/data/fish_data.csv')
reg_data = pd.read_csv('./static/data/perch_data.csv')

fish_input = cls_data[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target = cls_data['Species'].to_numpy()

kn = KNeighborsClassifier()
kn.fit(fish_input,fish_target)

'''
fish class
'''
@ml.route("/fishcls",methods=['GET','POST'])
def fishcls():
    if request.method=='POST':
        print(request.form["weight"])
    fish_input = cls_data[['Weight','Length','Diagonal','Height','Width','Species']].to_numpy()
    fish_target = cls_data['Species'].to_numpy()
    fish_target = np.unique(fish_target)
    pred = kn.predict([[50,60,70,30,40]])
    print(pred)
    return render_template("ml/fishcls.html",fish_input=fish_input,fish_target=fish_target)

@ml.route("/img1/<int:x>/<int:y>")
def legnthweightimg(x,y):
    plt.figure(figsize=(13,6))
    plt.subplot(1,2,1)
    plt.title('길이와 무게 그래프')
    breamindex = cls_data['Species']=='Bream'
    roachindex = cls_data['Species']=='Roach'
    perchindex = cls_data['Species']=='Perch'
    smeltindex = cls_data['Species']=='Smelt'
    parkkiindex = cls_data['Species']=='Parkki'
    Whitefishindex = cls_data['Species']=='Whitefish'
    Pikeindex = cls_data['Species']=='Pike'
    legnth = cls_data["Length"].to_numpy()
    weight = cls_data["Weight"].to_numpy()
    if x is None:
        x,y = np.random.randint(1,100,2)
    plt.scatter(legnth[breamindex],weight[breamindex],c='#ff0000')
    plt.scatter(legnth[roachindex],weight[roachindex],c='#00ff00')
    plt.scatter(legnth[perchindex],weight[perchindex],c='#0000ff')
    plt.scatter(legnth[smeltindex],weight[smeltindex],c='#000f00')
    plt.scatter(legnth[parkkiindex],weight[parkkiindex],c='#0f0000')
    plt.scatter(legnth[Whitefishindex],weight[Whitefishindex],c='#fff000')
    plt.scatter(legnth[Pikeindex],weight[Pikeindex],c='#770fff')
    plt.scatter(x,y)
    plt.xlabel('길이')
    plt.ylabel('무게')
    plt.legend(['bream','roach','perch','smelt','parrki','whitefish','Pike'])
    plt.subplot(1,2,2)
    plt.title('대각선과 두께 그래프')
    Diagonal = cls_data["Diagonal"].to_numpy()
    Width = cls_data["Width"].to_numpy()
    if x is None:
        x,y = np.random.randint(1,100,2)
    plt.scatter(Diagonal[breamindex],Width[breamindex],c='#ff0000')
    plt.scatter(Diagonal[roachindex],Width[roachindex],c='#00ff00')
    plt.scatter(Diagonal[perchindex],Width[perchindex],c='#0000ff')
    plt.scatter(Diagonal[smeltindex],Width[smeltindex],c='#000f00')
    plt.scatter(Diagonal[parkkiindex],Width[parkkiindex],c='#0f0000')
    plt.scatter(Diagonal[Whitefishindex],Width[Whitefishindex],c='#fff000')
    plt.scatter(Diagonal[Pikeindex],Width[Pikeindex],c='#770fff')
    plt.scatter(x,y)
    plt.xlabel('대각선')
    plt.ylabel('두께')
    plt.legend(['bream','roach','perch','smelt','parrki','whitefish','Pike'])
    img = BytesIO()
    plt.savefig(img,format="png",dpi=100)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

'''
fish reg
'''
@ml.route("/fishreg")
def fishreg():
    fish_input = reg_data[['length','height','width','weight']].to_numpy()
    return render_template("ml/fishreg.html",fish_input=fish_input)

