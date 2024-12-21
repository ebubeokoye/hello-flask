from cs50 import SQL
from flask import Flask, render_template, request

app=Flask(__name__)

db=SQL("sqlite:///froshims.db"")

SPORTS= [
    "Basketball"
    "Soccer"
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html")

#lets validate input
@app.route("/register", methods=["POST"])
def register():
    name=request.form.get("name")
    sport=request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")y
    
# to deregister
id=request.form.get("id")
if id:
    db.execute("DELETE FROM registrants WHERE id=?", id)

