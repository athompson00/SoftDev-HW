from flask import Flask, render_template
import urllib, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    return render_template("index.html")

@app.route("/taco") #assign following fxn to run when root route requested
def taco():
    u = urllib.request.urlopen(" http://taco-randomizer.herokuapp.com/random")
    response = u.read()
    data = json.loads(response)
    recipe = data["shell"]["recipe"]
    return render_template("fancyTaco.html", display = recipe)

@app.route("/rnm") #assign following fxn to run when root route requested
def rnm():
    u = urllib.request.urlopen("https://rickandmortyapi.com/api/character/")
    response = u.read()
    data = json.loads(response)
    recipe = data["results"][0]
    return render_template("rickAndMorty.html", display = recipe)

@app.route("/quotes") #assign following fxn to run when root route requested
def quotes():
    u = urllib.request.urlopen("http://quotes.rest/qod.json?category=inspire")
    response = u.read()
    data = json.loads(response)
    recipe = data["contents"]["quotes"][0]
    return render_template("quote.html", display = recipe)


if __name__ == "__main__":
    app.debug = True
    app.run()
