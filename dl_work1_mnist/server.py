from flask import Flask, render_template, send_file,request
from tensorflow import keras
import myloaddata
import numpy as np

app = Flask(__name__)

model = keras.models.load_model('best-cnn-model.h5')

@app.route("/",methods=['GET','POST'])
def index():
    pred=""
    if request.method == 'GET' :
        print('get')
    else :
        f = request.files['file']
        f.save('temp.png')
        temp = myloaddata.tempread()
        pred = model.predict(temp)
        classes = ['티셔츠', '바지', '스웨터', '드레스', '코트','샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']
        pred = '업로드하신 파일은 '+classes[np.argmax(pred)]+'로 예측됩니다.'
    return render_template("index.html",pred=pred)


@app.route("/file/<fol>/<name>")
def filedown(fol,name):
    filename = "static/img/"
    if fol in 'train':
        filename = filename+'train/'+name+'.png'
    else :
        filename = filename+'val/'+name+'.png'
    return send_file(filename, as_attachment=True)


app.run(debug=True)
