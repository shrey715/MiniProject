import mysql.connector as sql
from tkinter import * 

#CREATES DATABASE AND TABLES ONLY
#TO BE RUN BEFORE FIRST EXECUTION

username=0
password=0

def sqlconnect():
    global username
    global password
    
    userValue=str(username.get())
    pwdValue=str(password.get())

    connect=sql.connect(host='localhost',user=userValue ,passwd=pwdValue)
    cur=connect.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS HOTEL_MANAGEMENT_SYSTEM") 
    connect.commit()
    connect.close()

    connect=sql.connect(host='localhost',user=userValue ,passwd=pwdValue ,database='HOTEL_MANAGEMENT_SYSTEM')
    cur=connect.cursor()

    cur.execute("create table if not exists Customer_Records(Customer_ID int primary key, Cname varchar(25), RoomNo int, PhoneNo char(10), Address varchar(100));")
    cur.execute("create table if not exists Room_Details(RoomNo int primary key, Check_In_Date date, Check_Out_Date date, Room_Bill int, Food_Bill int, Total_Bill int);")
    connect.commit()
    connect.close()

def mainwin():
    global username
    global password

    sqllogin = Tk()
    sqllogin.title("Initialisation")

    uname=Label(sqllogin,text="Username>>")
    uname.grid(column=1,row=1)
    username=Entry(sqllogin,width=20)
    username.grid(column=3,row=1)

    pwd=Label(sqllogin,text="Password>>")
    pwd.grid(column=1,row=2)
    password=Entry(sqllogin,show="*",width=20)
    password.grid(column=3,row=2)
    
    Login = Button(sqllogin, text="Login", command=sqlconnect)
    Login.grid(column=2,row=3)

    sqllogin.mainloop()