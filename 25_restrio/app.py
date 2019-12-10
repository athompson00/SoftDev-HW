from flask import Flask, render_template
<<<<<<< HEAD
import urllib3, json
=======
import urllib, json
>>>>>>> 7800b803c6d58a4ace3bac9f7783d4282ca9e2ff

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
<<<<<<< HEAD
    http = urllib3.PoolManager()
    response = http.request('GET', "http://taco-randomizer.herokuapp.com/random/")
    data = response.data
    dict = json.loads(data)
    print(dict["condiment"]["recipe"])
    input = dict["condiment"]["recipe"]
    return render_template("index.html", data = input)
=======
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
>>>>>>> 7800b803c6d58a4ace3bac9f7783d4282ca9e2ff


if __name__ == "__main__":
    app.debug = True
    app.run()
