from unicodedata import decimal
from flask import Blueprint,render_template,send_file,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.cluster import KMeans
import os
import random
import cv2

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

ml = Blueprint("ml",__name__,url_prefix="/ml")

cls_data = pd.read_csv('./static/data/fish_data.csv')
reg_data = pd.read_csv('./static/data/perch_data.csv')

fish_input = cls_data[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target = cls_data['Species'].to_numpy()

kn = RandomForestClassifier()
kn.fit(fish_input,fish_target)

train_df = pd.read_excel('./static/data/fs.xlsx', sheet_name='train')
train_input = train_df[['Father']].to_numpy()
train_target = train_df['Son'].to_numpy()

es = ExtraTreesRegressor()
es.fit(train_input,train_target)

fruits = np.load('./static/data/fruits_300.npy')
fruits2d = fruits.reshape(-1,10000)

km = RandomForestClassifier()
km.fit(fruits2d,np.array(['사과']*100+['파인애플']*100+['바나나']*100))

'''
fish class
'''
@ml.route("/fishcls",methods=['GET','POST'])
def fishcls():
    a,b,c,d,e=0,0,0,0,0
    pred='예측하고 싶은 데이터를 입력하세요'
    try:
        if request.method=='POST':
            a = float(request.form["weight"])
            b = float(request.form["length"])
            c = float(request.form["diagonal"])
            d = float(request.form["height"])
            e = float(request.form["width"])
            pred = kn.predict([[a,b,c,d,e]])
            pred = f"입력한 데이터의 예측값은 {pred[0]} 입니다"
    except:
        pass
    fish_input = cls_data[['Weight','Length','Diagonal','Height','Width','Species']].to_numpy()
    fish_target = cls_data['Species'].to_numpy()
    fish_target = np.unique(fish_target)
    return render_template("ml/fishcls.html",fish_input=fish_input,fish_target=fish_target,pred=pred)

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
@ml.route("/fsreg",methods=['GET','POST'])
def fishreg():
    pred='예측하고 싶은 데이터를 입력하세요'
    try:
        if request.method=='POST':
            a = float(request.form["father"])
            pred = es.predict([[a]])
            pred = f"입력한 데이터의 아들키는 {np.round(pred[0],decimals=2)} 입니다"
    except:
        pass
    return render_template("ml/fsreg.html",train_df=train_df[['Father','Son']].to_numpy(),pred=pred)

@ml.route("/img2/<int:x>/<int:y>")
def fatherson(x,y):
    plt.title('아빠와 아들키')
    plt.scatter(train_df['Father'],train_df['Son'])
    plt.xlabel('father')
    plt.xlabel('son')
    img = BytesIO()
    plt.savefig(img,format="png",dpi=100)
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

'''
fruitcluster
'''
@ml.route("/fruits",methods=['GET','POST'])
def fruitcluster():
    files_list = os.listdir("./uploads")
    pred='예측할 이미지를 다운받아서\n업로드하세요'
    try:
        if request.method=='POST':
            f = request.files['filename']
            f.save('./uploads/' + f.filename) # 파일명을 보호하기위한 함수, 지정된 경로에 파일 저장
            a = cv2.imread('./uploads/' + f.filename,cv2.IMREAD_GRAYSCALE)
            pred = km.predict(a.reshape(-1,10000))
            pred = f"업로드한파일은 {pred} 입니다"
    except Exception as e:
        print(e)
    return render_template("ml/fruits.html",train_df=train_df[['Father','Son']].to_numpy(),pred=pred)

# @ml.route("/img3/<int:x>/<int:y>")
# def fruitsimg(x,y):
#     _,axis = plt.subplots(1,10,figsize=(10,1))
#     rgen = randint(0,300)
#     ranary = rgen.rvs(10)
#     for i in range(10):
#         axis[i].imshow(fruits[ranary[i]],cmap='gray_r')
#         axis[i].axis('off')
#     # plt.imshow(fruits[0],cmap='gray_r')
#     img = BytesIO()
#     plt.savefig(img,format="png",dpi=100)
#     plt.close()
#     img.seek(0)
#     return send_file(img, mimetype='image/png')

# @ml.route("/img4")
# def fruitsimg4():
#     _,axis = plt.subplots(1,3,figsize=(4,1))
#     means = km.cluster_centers_.reshape(-1,100,100)
#     for i in range(3):
#         axis[i].imshow(means[i],cmap='gray_r')
#         axis[i].axis('off')
#     # plt.imshow(fruits[0],cmap='gray_r')
#     img = BytesIO()
#     plt.savefig(img,format="png",dpi=200)
#     plt.close()
#     img.seek(0)
#     return send_file(img, mimetype='image/png')    

@ml.route("/ranimg1/")
def ranimg1():
    np.random.seed(a=None)
    rgen = np.random.randint(0,100, size=1)
    print(rgen)
    return send_file(f'./static/data/fruits/fruits{rgen[0]}.png',
                    as_attachment=True)

@ml.route("/ranimg2/")
def ranimg2():
    np.random.seed(a=None)
    rgen = np.random.randint(100,200, size=1)
    print(rgen)
    return send_file(f'./static/data/fruits/fruits{rgen[0]}.png',
                    as_attachment=True)

@ml.route("/ranimg3/")
def ranimg3():
    np.random.seed(a=None)
    rgen = np.random.randint(200,300, size=1)
    print(rgen)
    return send_file(f'./static/data/fruits/fruits{rgen[0]}.png',
                    as_attachment=True)