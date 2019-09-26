from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def occupation():
    return render_template('test.html')

@app.route("/auth")
def stuff():
    print(request.form)
    print(app)
    print(request)
    return render_template('auth.html', username = request.args["username"])


if __name__ == "__main__":
    app.debug = True
    app.run()
