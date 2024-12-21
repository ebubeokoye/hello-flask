from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/DOB", methods=["GET", "POST"])
def DOB():
    if request.method=="POST":
        return render_template("DOB.html")