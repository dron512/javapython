from flask import Flask, render_template,request
from ml.knclf import MyKNclf
import cv2

app = Flask(__name__)
kclf = MyKNclf().getModel()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/KNeighbors",methods=['GET','POST'])
def test():
    pred = '파일을 업로드 하셔야 합니다.'
    if request.method=='GET':
        pass
    elif request.method=='POST':
        f = request.files['filename']
        f.save('upload.png')
        try:
            data = cv2.imread('upload.png',cv2.IMREAD_GRAYSCALE)
            pred = kclf.predict(data.reshape(-1,25))
            pred = f'업로드하신 파일의 타겟값은 {pred}입니다'
        except Exception as e:
            print(e)
            pred = e
    return render_template("KNeighbors.html",pred=pred)

if __name__ =='__main__':
    app.run(debug=True)