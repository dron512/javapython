from flask import Flask,render_template,request
from calresult import returnResult

app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    result = returnResult(request.args.get("num1"),request.args.get("num2"))

    return render_template("index.html",result=result)

app.run(debug=True,host="127.0.0.1",port=5000)