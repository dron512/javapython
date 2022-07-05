from flask import Flask,render_template

app = Flask(__name__,template_folder="templates")

@app.route('/')
def hello_world():
    num = 10
    myst = "DB에서 읽었는 내용"
    return render_template('index.html',num=num,myst=myst)

@app.route('/aa')
def aa():
    return "aa"

@app.route('/bb')
def bb():
    return "bb"

@app.route('/cc')
def cc():
    return "cc"