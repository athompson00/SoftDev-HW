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

#hardcoded correct login information
username = "alex"
password = "pass"

#initial route, renders home.html/our login page
@app.route("/")
def login():
    global entered
    entered = False #initialize entered and set to false, as no information has yet been entered

    #create global variables, which will store user submitted info
    global userw
    userw = ""
    global passw
    passw = ""

    return render_template('home.html', error = entered)

@app.route("/welcome")
def stuff():
    entered = False #reset entered variable

    #necessary form stuff
    print(request.form)
    print ("????????")
    print(request.method)
    print(app)
    print(request)

    userw = request.args["username"] #set userw to submitted username
    passw = request.args["password"] #set passw to submitted password

    #session["username"] = request.args["username"]

    if (request.args["username"] == username) & (request.args["password"] == password): #if username and password are correct, redirect to welcome page
        return render_template('welcome.html', username = request.args["username"], password = request.args["password"])
    else: #if incorrect, redirect to login page with error message
        return redirect(url_for('elogin'))

@app.route("/oops")
def elogin():
    #set entered to true, user submitted incorrect login information
    entered = True

    return render_template('home.html', error = entered, passw = passw, userw = userw)

if __name__ == "__main__":
    app.debug = True
    app.run()
