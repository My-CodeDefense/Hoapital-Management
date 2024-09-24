import sqlite3
from tabulate import tabulate

try:
    db = sqlite3.connect("Hospital.db")
except:
    print('Fail... ')
cursor = db.cursor()

#cursor.execute("""Drop Table If Exists Patients""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Patients(
id VARCHAR PRIMARY KEY, 
Name TEXT NOT NULL,
dob INTEGER NOT NULL, 
Gender TEXT NOT NULL, 
Adhar INTEGER NOT NULL, 
Mobile_No INTEGER NOT NULL, 
Blood_Group TEXT,
Doctor_Name TEXT NOT NULL,
Date INT)""")

def patient() :
    name = input("Enter Name of Patient:- ")
    dob = input("Enter Date of birth (DDMMYYYY) :- ")
    mob = input ("Enter Mobile Number:- ")
    sec = input("Enter Gender M/F :- ")
    adh = input("Enter Adhar No (Last 4 Digits) :- ")
    blood = input("Enter Blood Group:- ")
    doc = input("Enter Doctor's Name:- ")
    date = input("Enter Date For Appointnent (DDMMYYYY) :- ")
    date = str(date)
    id = name[0:2] + dob[:4]
    dob = dob[0:2]+"/"+dob[2:4]+"/"+dob[4:8]
    date = date[0:2]+"/"+date[2:4]+"/"+date[4:8]
    drn = "Dr. "+doc.capitalize()
    cursor.execute("""INSERT INTO Patients(id, Name, Mobile_No, Gender, Adhar,DOB, Blood_Group, Doctor_Name, Date) VALUES (?,?,?,?,?,?,?,?,?)""",(id.capitalize(),name.capitalize(),mob, sec.upper(), adh, dob,blood.upper(), drn, date))
    print("Patient's Appointment Sucessfully Granted...")
    
    print("Your Id for Appointment is :- ",id," Date for Appointment :- ",date) 
    db.commit()
     
def data_by_id(record_id):
    cursor.execute('SELECT * FROM Patients WHERE id = ?', (record_id,))
    row = cursor.fetchone()
    data = row
    if data:
        headers = ["Id", "Name", "DOB", "Gender","Adhar", "Mobile", "Blood"," Doctor","Appointment"]
        print(tabulate([data], headers=headers, tablefmt="grid"))
    else:
        print(f"No record found with ID {record_id}")
        
def data_by_name(nm, mb,dt):
    cursor.execute('SELECT id FROM Patients WHERE Name = ? AND Mobile_No = ? AND Date = ?', (nm, mb,dt))
    row = cursor.fetchone()
    data = row
    if data:
        headers = ["Id"]
        print(tabulate([data], headers=headers, tablefmt="grid"))
    else:
        print("No record found")
