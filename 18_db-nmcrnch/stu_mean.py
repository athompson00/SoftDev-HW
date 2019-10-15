#Alex Olteanu and Alex Thompson
#SoftDev Period 2
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE= "glit.db"
db = sqlite3.connect("glit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#create table
command = "CREATE TABLE stu_mean(name TEXT, id INTEGER, average INTEGER);"
c.execute(command) # run SQL statement

#calculates the average of a student given their id
def calcAvg(id):
    command = "SELECT * FROM courses"
    c.execute(command)
    data = c.fetchall()
    totalPts = 0
    numCourses = 0
    for row in data:
        if row[2] == id:
            totalPts += row[1]
            numCourses += 1
    avg = totalPts / numCourses
    return avg

#returns name of a student given their id
def fetchName(id):
    command = "SELECT * FROM students"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[2] == id:
            return(row[0])

#insert data into table given an id
def insertData(id):
    command = "INSERT INTO stu_mean(name,id,average) VALUES" + "(" + "'" + str(fetchName(id)) + "'" + "," + str(id) + "," + str(calcAvg(id)) + ");"
    c.execute(command)

insertData(1)
insertData(2)
insertData(3)
insertData(4)
insertData(5)
insertData(6)
insertData(7)
insertData(8)
insertData(9)
insertData(10)

#prints table
select = "SELECT * FROM stu_mean"
stuff = c.execute(select)
for row in stuff:
    print(row)
#==========================================================

db.commit() #save changes
db.close()  #close database
