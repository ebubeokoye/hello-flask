from flask import Flask, redirect, render_template, request

app =Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

from flask import Flask, redirect, render_template, request, jsonify

app =Flask (__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def  process():

    # retrieve the data sent from javascript ie value
    data=request.get_json()

    # process the data using python code. here the data is multiplied by 2
    result = data['value'] * 2

    # return the result to the javascript function and shown in the div with id="output"
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/login")
def login():
    return render_template("login.html")