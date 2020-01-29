from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods = ["POST"])
def occupation():
    #print (request.args["username"])
    return render_template('test.html')

@app.route("/auth", methods = ["POST", "GET"])
def stuff():
    print(request.form)
    print ("????????")
    print(request.method)
    print(app)
    print(request)
    if request.args["username"] != "":
        return render_template('auth.html', username = request.args["username"])
    else:
        return render_template('noname.html')



if __name__ == "__main__":
    app.debug = True
    app.run()
