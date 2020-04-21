# Alex Thompsen
# SoftDev pd 2
# K18: come up for air
# 2020-03-05

import json
import csv
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

def getscores(year):
    scores = []
    schools_list = {}
    with open('static/json/scores' + str(year) + '.json') as json_file:
        schools = json_file.read()
        schools_list = json.loads(schools)
        schools_list = schools_list['data']
    for school in schools_list:
        #print(school)
        if (school[11] != None and school[11] != 's'):
            # print(school[11])
            # print(school[12])
            # print(school[13])
            # print('\n')
            scores.append(float(school[11]) + float(school[12]) + float(school[13]))
    return scores

def cachescores(vals2010, vals2012):
    with open('static/csv/2010.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['score'])
        for val in vals2010:
            filewriter.writerow([str(val)])
    with open('static/csv/2012.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['score'])
        for val in vals2012:
            filewriter.writerow([str(val)])



@app.route('/')
def landing():
    values2010 = getscores(2010)
    values2012 = getscores(2012)
    #cachescores(values2010, values2012)
    return render_template("index.html", values2010 = values2010, values2012 = values2012)

if __name__ == "__main__":
        app.debug = True
        app.run()
