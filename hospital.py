import sqlite3
from patients import patitents 
from doctors import doctors
from patientup import update
try:
    db = sqlite3.connect("Hospital.db") #if recordings will remove the test.db will be create in Internal Storage
except:
    print('Fail... ')    
cursor = db.cursor()

def Patients_Login() :
    print("""Press 1 for Appointment""")
    print("""Press 2 for Checking Appointment """)
    print("""Press 3 if You forgot your Id""")
    print()
    y = int(input('Enter your Response:- '))
    if y == 1:
        print() 
        print(" Doctor's List ") 
        doctors.data_dr()
        patitents.patient()
    if y == 2:
        print() 
        record_id = input("Enter your Id:- ")
        patitents.data_by_id(record_id)
    if y == 3:
        nm = input("Enter your Name:- ")
        mobile = int(input("Enter Your Mobile Number :- "))
        print() 
        dt = input("Enter Date of Appointnent:- ")
        ndt = dt[0:2]+"/"+dt[2:4]+"/"+dt[4:8]
        patitents.data_by_name(nm.capitalize(), mobile,ndt)

def Administration_Login():
    print("""
    Press 1 for Check All Appointments
    Press 2 for List of Doctors
    Press 3 for Adding Doctors
    Press 4 for Cancel Appointment
    Press 5 for Update Appointment""")
    choice = int(input("Enter Command :- "))
    if choice == 1:
        print()
        print("List of All Appointments:-")
        doctors.all_data_pt()
    if choice == 2:
        print()
        doctors.all_data_dr()
    if choice == 3:
         doctors.add_doctor()
    if choice == 4:
        id = input("Enter ID:- ")
        update.delete_record(id)
    if choice == 5:
        id = input("Enter ID:- ")
        print('''   
        Press 0 For Update Name
        Press 1 For Update dob
        Press 2 For Update Appointment Date
        Press 3 For Update Phone No
        Press 4 For Update Adhar
        Press 5 For Update Blood Group''') 
        what_upd = int(input("What to Update:- ") ) 
        new = input("Updated Entry :- ")
        update.pt_upd(what_upd,new,id)
    
t = 1
print('      '*6,'Hospital Management System')
print("""Press 1 for Login as Patitent
Press 2 for Login as Administrator""") 
print()
who = int(input("Login as :- "))
if who == 2:
    credentials = {"Ram":"980"}
    print()
    username = input('Enter Username :- ')
    password = input('Enter Password:- ') 
print()
while t==1:    
    try:
        print('Welcome... ')
        if who == 1:
            Patients_Login()
            print()
            print('''Do you want to continue 
Press 0 for No
Press 1 for Yes''')
            t = int(input("Response:- "))
            if t != 1:
                break
        elif who == 2:    
            if username.capitalize() in credentials:
                if credentials[username.capitalize()] == password:
                    Administration_Login()
                    print()
                    print('''Do you want to continue 
Press 0 for No
Press 1 for Yes''')
                    t = int(input("Response:- "))
                    if t!= 1:
                        break
                else:
                    print('Incorrect Password')
                    break                  
            else:
                print("Incorrect Username") 
                break               
        else:
           print('Wrong Response!! ')
    except:
        print("Invalid Entry")
else:
    print('       Time out....  ')