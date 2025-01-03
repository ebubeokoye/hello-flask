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
            return redirect("/login")
        else:
            return redirect("/registered")
    return redirect("/registered")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/validatelogin", methods=["POST"])
def validatelogin():
    connection=sqlite3.connect("signup.db")
    db=connection.cursor()

    email=request.form.get("email")
    password=request.form.get("password")
    if not email:
        return redirect("/login")
    if not password:
        return redirect("/login")

    return render_template("registered.html")

@app.route("/registered")
def registered():
    return render_template("registered.html")