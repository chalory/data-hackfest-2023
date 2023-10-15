from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        message = ""
        result = 0.8
        
        if 0 < result <= 0.2:
            message = "You are very healthy! You are at little to no risk of heart failure"
        elif 0.2 < result <= 0.5:
            message = "You are well! You are at moderate risk of heart failure"
        elif 0.5 < result <= 0.8:
            message = "You are at risk! You are at above-average risk of heart failure" 
        elif 0.8 < result <= 1.0:
            message = "You are at severe risk of heart failure! Please seek medical attention!"

        return render_template("results.html", msg=message)
    
