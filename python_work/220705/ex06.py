from flask import Flask,render_template
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__,template_folder="templates")

knclf = KNeighborsClassifier(n_neighbors=1)
knclf.fit([[200,300],[250,350],[300,250],[50,50],[40,45]],
            ['의자','의자','의자','마우스','마우스'])

@app.route('/')
def hello_world():
    num = 10
    myst = "DB에서 읽었는 내용"
    return render_template('index.html',num=num,myst=myst)

@app.route('/aa')
def aa():
    result = knclf.predict([[380,250]])
    return "aa"+str(result)

@app.route('/bb')
def bb():
    return "bb"

@app.route('/cc')
def cc():
    return "cc"

