from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "no hablo queso";

@app.route("/stub")
def stub():
    nums = [2,1,5,6,7,4,3,2,34,5];
    return render_template("stub.html", nums=nums);

if __name__ == "__main__":
    app.debug = True
    app.run()
