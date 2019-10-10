#Alex "Thumb" Thompson
#SoftDev pd. 2
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


command = "CREATE TABLE students (name TEXT PRIMARY KEY, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

with open ("students.csv", "r") as csvfile :
    filereader = csv.reader("students.csv")
    for row in filereader:
        command = "INSERT INTO students VALUES (" + "'" + row["name"] + "', " + row["age"] + row["id"] + ");"
        c.execute(command)





command = "CREATE TABLE courses (code, mark INTEGER, id INTEGER);"
c.execute(command)

with open ("courses.csv", "r") as csvfile :
    filereader = csv.reader("courses.csv")
    for row in filereader:
        command = "INSERT INTO students VALUES (" + "'" + row["code"] + "', " + row["mark"] + row["id"] + ");"
        c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
