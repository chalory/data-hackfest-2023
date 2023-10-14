from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    if(request.method == "POST"):
        print(request.form)
    return render_template("index.html")
