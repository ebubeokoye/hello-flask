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

@app.route("/createaccount-land-agent")
def createaccountlandtagent():
    return render_template("createaccount-land-agent.html")

@app.route("/createaccount-housing-agent")
def createaccounthousingagent():
    return render_template("createaccount-housing-agent.html")

# when the user clicks on Buy from the landing page
@app.route("/buylinkfrompage2", methods=["POST"])
def buylinkfrompage2():
    return render_template("buylinkfrompage2.html")

# this section is for the user after they've registered/logged in
@app.route("/homepage", methods=["GET", "POST"])
def homepage(): 
    if request.method == "POST":
        return render_template("homepage.html")
    else: 
        return render_template("homepage.html")
    
# user buy land listing
@app.route("/buyland")
def buyland(): 
    return render_template("user-buyland.html")

@app.route("/user_oneacre_buyland_listingpg2")
def user_oneacre_buyland_listingpg2():
    return render_template("user-oneacre-buyland-listingpg2.html")

@app.route("/user_viewdetails_general_form")
def user_viewdetails_general_form():
    return render_template("user-viewdetails-general-form.html")




@app.route("/rent")
def rent(): 
    return render_template("user-rent.html")

@app.route("/houseitems")
def houseitems(): 
    return render_template("houseitems.html")

@app.route("/user-account")
def useraccount(): 
    return render_template("user-account.html")

# this section is for the land agent

@app.route("/land_agent_homepage", methods=["GET", "POST"])
def land_agent_homepage():
    if request.method == "POST":
        return render_template("landagent-homepage.html")
    else:
        return render_template("landagent-homepage.html")
    
@app.route("/agent_land_listing", methods=["GET", "POST"])
def agent_land_listing():
    if request.method == "POST":
        return redirect("/agent_land_listing")
    else:
        return render_template("agent-land-listing.html")
        
@app.route("/landing_agent_oneacre_listingpg2", methods=["GET", "POST"])
def landing_agent_oneacre_listingpg2():
    if request.method == "POST":
        return render_template("landing-agent-oneacre-listingpg2.html")
    else:
        return render_template("landing-agent-oneacre-listingpg2.html")

# this section is for the housing agent

@app.route("/housing_agent_homepage", methods=["GET", "POST"])
def housing_agent_homepage():
    if request.method =="POST":
        return render_template("housing-agent-homepage.html")
    else:
        return render_template("housing-agent-homepage.html")
# items listing
@app.route("/agent_housing_listing", methods=["GET", "POST"])
def agent_housing_listing():
    if request.method == "POST":
        return render_template("agent-housing-listing.html")
    else:
        return render_template("agent-housing-listing.html")

@app.route("/housing_agent_bungalow_listingpg2",  methods=["GET", "POST"])
def housing_agent_bungalow_listingpg2():
    if request.method == "POST":
        return render_template("housing-agent-bungalow-listingpg2.html")
    else:
        return render_template("housing-agent-bungalow-listingpg2.html")


@app.route("/form_to_add_item_housingagent")
def form_to_add_item_housingagent():
    return render_template("form-to-add-item-housingagent.html")

@app.route("/form_to_edit_item_housingagent")
def form_to_edit_item_housingagent():
    return render_template("edit-item-houseagent.html")

# Insights section
@app.route("/insights_page_housingagent")
def insights_page_housingagent():
    return render_template("insightspage-housingagent.html")

# this section is for the vendor after they've registered/logged in
@app.route("/vendor_homepage", methods=["GET", "POST"])
def vendor_homepage():
    if request.method == "POST":
        return render_template("vendor-homepage.html")
    else:
        return render_template("vendor-homepage.html")
    
@app.route("/vendor_listing", methods=["GET", "POST"])
def vendor_listing():
    if request.method == "POST":
        return render_template("vendor-listing.html")
    else:
        return render_template("vendor-listing.html")
    
@app.route("/vendor_kitchenitems_listingpg2", methods=["GET", "POST"])
def vendor_kitchenitems_listingpg2():
    if request.method == "POST":
        return render_template("vendor-kitchenitems-listingpg2.html")
    else:
        return render_template("vendor-kitchenitems-listingpg2.html")
    