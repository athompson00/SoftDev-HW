# Alex Thompson (Thumb Thompson)
# William Cao (Cow)
# SoftDev1 pd2
# K10 -- <Jinja Tuning/Flask&Jinja/Learning to use jinja>
# 2019-09-23

from flask import Flask, render_template
import csv
import random

app = Flask(__name__) #create instance of class Flask

@app.route("/")
def hello_world():
    return "use route /occupyflaskst";

@app.route("/occupyflaskst")
def occupy_flask_st():
    job = randomJob()
    occupations = get_occupations()
    for occupation in occupations:
        occupations[occupation] = str(occupations[occupation])
    return render_template("stub.html", job = job, occupations = occupations);


def get_occupations():
    occupations = {} # Key: Occupation string Value: Percent in float
    with open('./data/occupations.csv', mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            occupations[row["Job Class"]] = float(row["Percentage"])
    del occupations['Total']  # Only keep track of jobs, not a total field
    return occupations

def randomJob():
    """
    Choose a random job weighted off of percent of population in the given population
    """
    occupations = get_occupations()
    job = random.randint(0, 997)  # ignores last row, which is not a occupation but a total field
    total = 0;  # To choose a random weighted, we need to set a range of numbers that corresponds to the percent
    for key in occupations:
        total += occupations[key]
        # multiply by 10 to make integer like comparison
        if (total * 10 >= job):
            return key


if __name__ == "__main__":
    app.debug = True
    app.run()
