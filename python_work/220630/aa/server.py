from flask import Flask, render_template, request, redirect, url_for
from sklearn.linear_model import LinearRegression

app = Flask(__name__, static_folder='./flask/static/',
            template_folder='./flask/templates/')

app.route("/")


app.run()