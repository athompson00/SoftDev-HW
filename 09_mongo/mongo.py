from pymongo import MongoClient
from bson.json_util import loads
import json

client = MongoClient()
db = client.db

collection = db.restaurants

collection.delete_many({})

file = open("primer-dataset.json", "r")
content = file.readlines()
for line in content:
    collection.insert_one(loads(line))

def getinborough(borough):
    return collection.find({"borough": borough})

def getinzip(zip):
    return collection.find({"address.zipcode": zip})

def getbyzipgrade(zip, grade):
    return collection.find({"address.zipcode": zip, "grades.0.grade": grade})

def getbyzipbelowscore(zip, score):
    return collection.find({"grades.0.score": {"$lt": score}, "address.zipcode": zip})

def getnearby(lon, lat):
    return collection.find({"address.coord.0": {"$lt": lon}, "address.coord.1": {"$lt": lat}})
