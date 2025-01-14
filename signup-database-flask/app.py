from flask import Flask, redirect, render_template, request

import sqlite3


app=Flask(__name__)

GENDERS=["Female", "Male"]
#lets connect the database to RAM

# create a cursor() method to be able to execute sql queries using python

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signuppage1")
def signuppage1():
    return render_template("signuppage1.html", genders=GENDERS)

@app.route("/validatepage1", methods=["POST"])
def validatepage1():

    connection=sqlite3.connect("signup.db")
    db=connection.cursor()

    email=request.form.get("email")
    password=request.form.get("password")
    firstname=request.form.get("firstname")
    lastname=request.form.get("lastname")
    
    if not email:
        return redirect("/")
    if not password:
        return redirect("/")
    if not firstname:
        return redirect("/")
    if not lastname:
        return redirect("/")
    if request.form.get("gender") not in GENDERS:
        return redirect("/")
    
    data=db.execute("SELECT email FROM signup WHERE email='" + email +"'")
    datalist=data.fetchall()
    for item in datalist:
        if email in item:
            return render_template("signuperror.html")
        else:
            return redirect("/uploadimage")
    return redirect("/uploadimage")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/validatelogin", methods=["POST"])
def validatelogin():
    connection=sqlite3.connect("signup.db")
    db=connection.cursor()

    email=request.form.get("email")
    password=request.form.get("password")

    data=db.execute("SELECT email, password FROM signup WHERE password='" + password +"'")
    datalist=data.fetchall()
    print(datalist)
    for item in datalist:
        if password in item:
            if email in item:
                return render_template("welcome!(after-login).html")
            else:
                return redirect("/login")
        else:
            return redirect("/login")
    return redirect("/login")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgot-password.html")
    
@app.route("/smscodeforforgotpassword", methods=["POST"])
def smscodeforforgotpassword():
    number=request.form.get("phone number")
    if not number:
        return redirect("/smscodeforforgotpassword")
    else:
        return render_template("smscode-for-forgot-password.html")

@app.route("/uploadimage")
def uploadimage():
    return render_template("uploadimage.html")

@app.route("/registered", methods=["POST"])
def registered():
    if 'file' not in request.files:
        return redirect("/uploadimage")
    else:
        return render_template("registered.html")
    