from flask import Flask, render_template, send_file,request
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array 
import numpy as np

app = Flask(__name__)

model = keras.models.load_model('best-catdog-cnn-model.h5')

@app.route("/",methods=['GET','POST'])
def index():
    pred=""
    if request.method == 'GET' :
        print('get')
    else :
        try:
            f = request.files['file']
            f.save('temp.png')
            img = load_img('temp.png', target_size=(150, 150))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict(images)
            if classes[0] > 0:
                pred = '업로드하신 파일은 개로 예측됩니다.'
            else:
                pred = '업로드하신 파일은 고양이로 예측됩니다.'
        except:
            pred="파일업로드 실패했습니다. 다시시도하세요"
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
