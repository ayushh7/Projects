import mysql.connector as sq
mydb=sq.connect(host="localhost",user="NIKHIL",password="nikhil2003R")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists kv3;")
mycursor.execute("use kv3")
#creating required tables 
mycursor.execute("create table if not exists smsrecord(rnno char(4), name varchar(10))")
mydb.commit()
while(True):
    
    print("1=ADD NEW RECORD")
    print("2=UPDATE/MODIFY RECORD")
    print("3=DELETE RECORD")
    print("4=DISPLAY RECORD")
    print("5=EXIT")
    ch=int(input("Enter your choice:"))

    #PROCEDURE FOR ADDING RECORD 
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        rnno=str(input("Enter Roll Number:"))
        name=input("Enter name:")
        mycursor.execute("insert into smsrecord values('"+rnno+"','"+name+"')")
        mydb.commit()
        print("Record is successfully created!!!")
        
#PROCEDURE FOR UPDATIONG NAME OF STUDENT
    elif(ch==2):
        acno=str(input("Enter Roll Number:"))
        nm=input("Enter name:")
        mycursor.execute("update smsrecord set name='"+nm+"' where rnno='"+acno+"'")
        mydb.commit()
        print("Record  has been updated successully!!!")
#PROCEDURE FOR DELETING THE RECORD

    elif(ch==3):
        x=str(input("Enter Roll Number:"))
        mycursor.execute("delete from smsrecord where rnno='"+x+"'")
        mydb.commit()
        print("Record has been deleted suceesfully ")

#PROCEDURE FOR DISPLAYING ALL RECORDS
    elif(ch==4):
        mycursor.execute("select * from smsrecord")
        for i in mycursor:
            print(i)
    else:
        break
