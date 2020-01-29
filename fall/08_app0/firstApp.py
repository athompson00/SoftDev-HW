from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/music")
def melody():
    return "classical"

@app.route("/lacrosse")
def stick():
    return "sports"

@app.route("/compSci")
def melody():
    return "Software Development"

if __name__ == "__main__":
    app.debug = True
    app.run()
