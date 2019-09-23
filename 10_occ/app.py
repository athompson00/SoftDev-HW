from flask import Flask, render_template
import csv
import random
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "no hablo queso";

@app.route("/occupyflaskst")
def stub():
    job = randomJob()
    occupations = get_occupations()
    for occupation in occupations:
        occupations[occupation] = str(occupations[occupation])
    return render_template("stub.html", job = job, occupations = occupations);


def get_occupations():
    occupations = {}
    with open('./data/occupations.csv', mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            occupations[row["Job Class"]] = float(row["Percentage"])
    return occupations

def randomJob():
    occupations = get_occupations()
    job = random.randint(0, 997)  ##ignores last row because of 997
    total = 0;
    for key in occupations:
        total += occupations[key]
        if (total * 10 >= job):
            return key


if __name__ == "__main__":
    app.debug = True
    app.run()
