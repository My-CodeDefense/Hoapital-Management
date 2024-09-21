import sqlite3
try:
    db = sqlite3.connect("Hospital.db") #if recordings will remove the test.db will be create in Internal Storage
except:
    print('Fail... ')    
cursor = db.cursor()

def delete_record(id) :
    que = ('''DELETE FROM Patients WHERE id = ?''') 
    cursor.execute(que, (id,))
    db.commit()
    print("sucess")
    db.commit()

def update_N(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET Name = ?
    WHERE id = ?
    ''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()

def update_DOB(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET dob = ?
    WHERE id = ?
    ''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()

def update_DOA(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET Date = ?
    WHERE id = ?
    ''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()
    
def update_Mob(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET Mobile_No = ?
    WHERE id = ?
    ''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()
    
def update_Ad(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET Adhar = ?
    WHERE id = ?
    ''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()
    
def update_Bg(new, id):
    
    update_command = ('''
    UPDATE Patients
    SET Blood_Group = ?
    WHERE id = ?''') 
    data = (new,id) 
    cursor.execute(update_command, data)
    db.commit()

def pt_upd(what_upd,new,id):
        if what_upd == 0:
            update_N(new, id) 
        elif what_upd== 1:
            new = new[0:2]+"/"+new[2:4]+"/"+new[4:8]
            update_DOB(new, id)
        elif what_upd == 2:
            update_Ad(new, id)
        elif what_upd == 3:
            update_Mob(new, id)
        elif what_upd == 4:
            new = new[0:2]+"/"+new[2:4]+"/"+new[4:8]
            update_DOA(new, id)
        elif what_upd == 5:
            update_Bg(new, id)
        else:
            print("Wrong Response") 