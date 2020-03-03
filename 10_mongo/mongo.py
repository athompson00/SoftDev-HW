#Derek Leung, Alex Thompson
#Softdeb pd 2
#K10 -- Import/Export Bank
#2020-03-04

"""
prize.json contains all nobel prize winners, as well as the year in which they won the prize and what they won the prize for.
http://api.nobelprize.org/v1/prize.json
To import the data, we first opened the json and read in the lines to a list. Then we used the json library to convert the json strings to dictionaries and inserted them one by one into the database.
"""

import json
from pymongo import MongoClient

client = MongoClient()
db = client.teamName
collection = db.events
if(collection.count() == 0):
    file = open("prize.json", "r")
    content = file.readlines()
    for line in content:
        collection.insert_one(json.loads(line))

def findTopic(topic):
    topic = topic.lower()
    data = collection.find({"prizes.category": topic})
    for thing in data:
        print(thing)
        print('\n')

def findYear(year):
    topic = topic.lower()
    data = collection.find({"prizes.year": year})
    for thing in data:
        print(data)
        print('\n')

findTopic("chemistry")
