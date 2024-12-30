from flask import Flask, redirect, render_template, request
app=Flask(__name__)

#lets connect the database to RAM
import sqlite3
connection=sqlite3.connect("signup.db")

# create a cursor() method to be able to execute sql queries using python
db=connection.cursor()

app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")

app.route("register", methods=["GET", "POST"])
def register():
    return render_template("register.html")