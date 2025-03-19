from flask import Flask, redirect, render_template, request, jsonify

app =Flask (__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registeras")
def registeras():
    return render_template("register-as.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/createaccount-user")
def createaccountuser():
    return render_template("createaccount-user.html")

@app.route("/createaccount-vendor")
def createaccountvendor():
    return render_template("createaccount-vendor.html")

@app.route("/createaccount-agent")
def createaccountagent():
    return render_template("createaccount-agent.html")

# when the user clicks on Buy from the landing page
@app.route("/buylinkfrompage2", methods=["POST"])
def buylinkfrompage2():
    return render_template("buylinkfrompage2.html")

# this section upto number.... is for the user after they've registered/logged in
@app.route("/homepage", methods=["GET", "POST"])
def homepage(): 
    if request.method == "POST":
        return render_template("homepage.html")
    else: 
        return render_template("homepage.html")

@app.route("/buyland")
def buyland(): 
    return render_template("user-buyland.html")

@app.route("/rent")
def rent(): 
    return render_template("user-rent.html")

@app.route("/houseitems")
def houseitems(): 
    return render_template("houseitems.html")

@app.route("/user-account")
def useraccount(): 
    return render_template("user-account.html")
