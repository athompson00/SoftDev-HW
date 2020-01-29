#Alex Thompson and Alex Olteanu
#SoftDev Period 2
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE= "glit.db"
db = sqlite3.connect("glit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
print("STUDENT NAME AGE")

#create a table for students.csv
command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
c.execute(command) # run SQL statement

#insert data into table for students.csv
with open('students.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        namec = row["name"] #for ease of coding
        agec = row["age"] #for ease of coding
        idc = row["id"] #for ease of coding
        command = "INSERT INTO students(name,age,id) VALUES" + "(" + "'" + namec + "'" + "," + agec + "," + idc + ");"
        c.execute(command)

#prints table for students.csv
select = "SELECT * FROM students"
stuff = c.execute(select)
for row in stuff:
    print(row)

print("")

print("CODE MARK ID")
#create a table for courses.csv
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(command) # run SQL statement

#insert data into table for courses.csv
with open('courses.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        codec = row["code"] #for ease of coding
        markc = row["mark"] #for ease of coding
        idc = row["id"] #for ease of coding
        command = "INSERT INTO courses(code,mark,id) VALUES" + "(" + "'" + codec + "'" + "," + markc + "," + idc + ");"
        c.execute(command)

#prints table for courses.csv
select = "SELECT * FROM courses"
stuff = c.execute(select)
for row in stuff:
    print(row)

#==========================================================

db.commit() #save changes
db.close()  #close database
