import sqlite3
from tabulate import tabulate

try:
    db = sqlite3.connect("Hospital.db") #if recordings will remove the test.db will be create in Internal Storage
except:
    print('Fail... ')    
cursor = db.cursor()

#cursor.execute("""Drop Table if Exists Doctors""")
cursor.execute(""" CREATE TABLE IF NOT EXISTS Doctors(
id VARCHAR PRIMARY KEY, 
Name TEXT NOT NULL,
DOB TEXT NOT NULL,
Gender TEXT NOT NULL,
Specialization TEXT NOT NULL, 
Mobile_No INTEGER NOT NULL)""")

def all_data_pt() :
    cursor.execute('SELECT * FROM Patients')
    rows = cursor.fetchall()
    data = rows
    headers = ["Id", "Name", "DOB", "Gender", "Adhar", "Mobile", "Blood"," Doctor","Appointment"]
    print(tabulate(data, headers=headers,tablefmt="grid"))

def data_dr() :
    cursor.execute('SELECT Name, Specialization FROM Doctors')
    rows = cursor.fetchall()
    data = rows
    headers = ["Name","Specialization"]
    print(tabulate(data, headers=headers,tablefmt="grid"))


def all_data_dr() :
    cursor.execute('SELECT * FROM Doctors')
    rows = cursor.fetchall()
    data = rows
    headers = ["ID","Name","DOB","Gender","Specialization"," Mobile"]
    print(tabulate(data, headers=headers,tablefmt="grid"))


def add_doctor():
    print()
    name = input("Enter Doctor Name :- ")
    Gender = input("Enter Gender :- ")
    Mobile_No = int(input("Enter Phone No:- "))
    DOB = input("Enter DOB (DDMMYYYY) :- ")
    Special = input("Enter Specialization :- ")
    Id = input("Enter Id:- ")
    DOB = DOB[0:2]+"/"+DOB[2:4]+"/"+DOB[4:8]
    cursor.execute(""" INSERT INTO Doctors(id, Name, DOB, Gender, Specialization,Mobile_No) VALUES(?,?,?,?,?,?)""",(Id.upper(),name.capitalize(), DOB, Gender.upper(),Special.capitalize(),Mobile_No))
    db.commit()