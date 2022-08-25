from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import mydata

app = Flask(__name__)
data = pd.read_csv('kisa.csv',encoding='euc-kr')

@app.route("/",methods=['GET','POST'])
def car():
    table_data = data[['종목명','년도','성별','필기시험접수','필기시험응시','필기시험합격','필기시험합격률(퍼센트)',
                    '실기시험접수','실기시험응시','실기시험합격','실기시험합격률(퍼센트)','자격취득자현황(명)']].to_numpy()
    if request.method == 'POST':
        print(request.form.getlist('xitem'))
    return render_template("index.html",table_data=table_data,mydata=mydata.columns)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
