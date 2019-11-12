from flask import Flask
import urllib, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    u = urllib.request.urlopen("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&api_key=W56Oyc2HC3Kpl9qXvqmkIawDe3MeQbaFe053pgJF")
    response = u.read()
    data = json.loads(response)
    print(data["photos"][0]['img_src'])
    return "No hablo queso!"


if __name__ == "__main__":
    app.debug = True
    app.run()
