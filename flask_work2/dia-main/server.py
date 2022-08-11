from flask import Flask,render_template,request
import dia

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    당뇨여부 = '데이터를 넣으세요.'
    a = 6
    f = 33.6
    if request.method=='POST':
        esti = dia.getModel()
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']
        f = request.form['f']
        g = request.form['g']
        age = request.form['age']

        당뇨여부 = esti.predict([[a,b,c,d,e,f,g,age]])
        if 당뇨여부[0] == 1:
            당뇨여부 = '죄송합니다 당뇨병 걸렸네요...'
        else:
            당뇨여부 = '축하합니다. 당뇨병 아닙니다...'
        # 당뇨여부 = esti.predict([[1.0,89,66,23,94,28.1,0.2,21]])
    return render_template("index.html",당뇨여부=당뇨여부,a=a,f=f)


app.run(debug=True)