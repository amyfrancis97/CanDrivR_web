from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import (url_for, current_app as app)
app = Flask(__name__, static_url_path='/static/')

@app.route("/")
def landing_page():
    return render_template("landingpage.html")

# favicon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='/images/favicon.png')

@app.route("/test")
def test_page():
    return render_template("testpage.html", testtext = "Hello", testlist = [1,2,3])

@app.route("/CanDrivR")
def CanDrivR_page():
    return render_template("CanDrivR.html", testtext = "Hello", testlist = [1,2,3])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)

