from flask import Flask, render_template
import urllib3, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    http = urllib3.PoolManager()
    response = http.request('GET', "http://taco-randomizer.herokuapp.com/random/")
    data = response.data
    dict = json.loads(data)
    print(dict["condiment"]["recipe"])
    input = dict["condiment"]["recipe"]
    return render_template("index.html", data = input)


if __name__ == "__main__":
    app.debug = True
    app.run()
