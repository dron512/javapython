from flask import Flask, render_template, request

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

from ml.knclf import MyKNclf
import cv2

app = Flask(__name__)
kclf = MyKNclf().getModel()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/KNeighbors", methods=['GET', 'POST'])
def test():
    pred1 = 'x0과 x1을 입력하셔야 합니다.'
    pred2 = '파일을 업로드 하셔야 합니다.'
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            x_train = np.array([[2, 1],[3, 2],[3, 4],[5, 5],[7, 5],[2, 5],[8, 9],[9, 10],[6, 12]])
            x_test = np.array([[9, 2],[6, 10],[2, 4]])
            y_train = np.array([3, 5, 7, 10, 12, 7, 13, 13, 12])
            y_test = np.array([13, 12, 6])

            knr = KNeighborsRegressor(n_neighbors=3)
            knr.fit(x_train,y_train)
            x,y = int(request.form['x0']),int(request.form['x1'])
            pred1 = knr.predict([[x,y]])
            pred1 = f'예측하신 타겟값은 = {pred1} 입니다'
        except Exception as e:
            print(e)
            pred1 = e
        try:
            f = request.files['filename']
            f.save('upload.png')
            data = cv2.imread('upload.png', cv2.IMREAD_GRAYSCALE)
            pred2 = kclf.predict(data.reshape(-1, 25))
            pred2 = f'업로드하신 파일의 타겟값은 {pred2}입니다'
        except Exception as e:
            print(e)
            pred2 = e
    return render_template("KNeighbors.html", pred1=pred1, pred2=pred2)


if __name__ == '__main__':
    app.run(debug=True)
