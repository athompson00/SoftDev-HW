# Brian Moses and Alex Thompsen
# SoftDev1 pd 2
# K11: mongoflask
# 2020-03-05

import json
from pymongo import MongoClient
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
client = MongoClient() # sets to localhost automatically
db = client.MosDB

client.drop_database('MosDB')
#destroying and recreating database

db = client.MosDB
col = db.movies

with open('movies.json') as json_file:
    movies_string = json_file.read()
    movies_list = json.loads(movies_string)
    col.insert_many(movies_list)

@app.route('/')
def landing():
    return render_template("index.html")

# gets all movies grossing greater than gross
@app.route('/gross_results')
def gross():
    lis = list(col.find({"US_Gross": {"$gt": int(request.args['gross'])}}))
    return render_template("index.html",
      message = "Showing all movies grossing greater than $" + request.args['gross'] + "USD:",
      gross = lis) #show inputted thing
    #return render_template("index.html")

# gets all movies with ratings higher the specified IMDB and Rotten Tomatoes ratings
@app.route('/ratings_results')
def ratings():
    lis = list(
                col.find({
                    "Rotten_Tomatoes_Rating": {"$gt": int(request.args['rotten_tomatoes'])},
                    "IMDB_Rating": {"$gt": int(request.args['imdb'])}
                })
            )
    return render_template("index.html",
      message = "Showing all movies with IMDB Ratings greater than " + request.args['imdb'] + " and Rotten Tomatoes scores greater than " + request.args['rotten_tomatoes'],
      ratings = lis)

# gets all movies released later than the specified year
@app.route('/year_results')
def year():
    lis = [movie for movie in col.find({}) if int(movie["Release_Date"][-4:]) > int(request.args['year'])]
    return render_template("index.html",
      message = "Showing all movies released after " + request.args['year'],
      year = lis)

#gets all movies of the specified genre
@app.route('/genre_results')
def genre():
    print(request.args)
    lis = [movie for movie in col.find({"Major_Genre": request.args['genre']})]
    return render_template("index.html",
      message = "Showing all movies of " + request.args['genre'] + " genre",
      genre = lis)

#tells you whether there is a movie whose director shares your name that has over 1000 IMDB votes
@app.route('/popular_results')
def popular():
    name = request.args['name']
    is_popular = False
    movies = list(col.find({}))
    for movie in movies:
        if (movie['Director'] != None and name in movie['Director'] and movie['IMDB_Votes'] > 1000):
            is_popular = True
    if (is_popular):
        return render_template("index.html", message = "Your name is popular!")
    return render_template("index.html", message = "Sorry, your name is not popular.")

if __name__ == "__main__":
        app.debug = True
        app.run(host = '0.0.0.0')
