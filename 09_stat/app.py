from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    nums = [0, 1, 1, 2, 3, 5, 8];
    return render_template("stub.html", nums=nums);

if __name__ == "__main__":
    app.debug = True
    app.run()
