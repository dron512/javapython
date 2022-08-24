from flask import Flask, render_template, send_file,request
from tensorflow import keras
import numpy as np

app = Flask(__name__)

model = keras.models.load_model('best-catdog-cnn-model.h5')

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
        classes = ['개', '고양이']
        pred = '업로드하신 파일은 '+classes[np.argmax(pred)]+'로 예측됩니다.'
    return render_template("index.html",pred=pred)


@app.route("/file/<data>/<dogcat>/<number>")
def filedown(data,dogcat,number):
    filename = "static/cats_and_dogs/"
    if data in 'train':
        filename = filename+'train/'+dogcat+'.'+number+'.jpg'
    else :
        filename = filename+'validation/'+dogcat+'.200'+number+'.jpg'
    return send_file(filename, as_attachment=True)


app.run(debug=True)
