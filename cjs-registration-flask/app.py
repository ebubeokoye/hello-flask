from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DOB", methods=["POST"])
def DOB():
    email=request.form.get("email")
    if not email:
        return "Failed"
    else:
        return render_template("DOB.html")

@app.route("/success", methods=["POST"])
def success():
    dob=request.form.get("dob")
    if not dob:
        return "failure"
    else:
        return render_template("success.html")