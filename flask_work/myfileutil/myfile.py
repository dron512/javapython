from flask import Blueprint,send_file

app = Blueprint("myfile", __name__)

@app.route("/filedown/<ox>")
def filedownox(ox):
    
    return f"ox = {ox}"