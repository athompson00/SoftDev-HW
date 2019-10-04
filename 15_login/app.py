#Team Alex- Alex Thompson and Alex Olteanu
#Softdev Period 2
# Due 2019-10-4

#setup
from flask import Flask, render_template, request
from flask import redirect
from flask import session
from flask import url_for
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)

global msg
#hardcoded correct login information
username = "alex"
password = "pass"

#initial route, renders home.html/our login page
@app.route("/")
def login():
    if "counter" in session:
        session["counter"] = session.get("counter") + 1
        if ((session["username"] != "alex") & (session["password"] != "pass")):
            msg = "Wrong username and password"
        elif (session["username"] != "alex"):
            msg = "Wrong username"
        else:
            msg = "Wrong password"

        if (session["username"] == username) & (session["password"] == password): #if username and password are correct, redirect to welcome page
            return render_template('welcome.html')
        else:
            return render_template('home.html', error = True, message = msg )
    else:
        session["counter"] = 1
        msg = ""
        return render_template('home.html', error = False)

@app.route("/welcome")
def stuff():
    entered = False #reset entered variable


    session["username"] = request.args["username"] #set userw to submitted username
    session["password"] = request.args["password"] #set passw to submitted password

    #session["username"] = request.args["username"]

    if (session["username"] == username) & (session["password"] == password): #if username and password are correct, redirect to welcome page
        return render_template('welcome.html', username = session["username"], password = session["password"])
    else: #if incorrect, redirect to login page with error message
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run()
