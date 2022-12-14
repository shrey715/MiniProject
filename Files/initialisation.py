import mysql.connector as sql
from tkinter import * 
from tkinter import messagebox

#CREATES DATABASE AND TABLES ONLY
#TO BE RUN BEFORE FIRST EXECUTION

username=0
password=0

def sqlconnect(x):
    global username, password
    
    u=open("Variables\SQLUsername.txt","w")
    p=open("Variables\SQLPassword.txt","w")

    file=open("Variables\InitialisationCheck.txt","w")
    userValue=str(username.get())
    pwdValue=str(password.get())

    u.write(userValue)
    p.write(pwdValue)
    u.close()
    p.close()

    connect=sql.connect(host='localhost',user=userValue, passwd=pwdValue)
    if connect.is_connected():
       check=1
    cur=connect.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS HOTEL_MANAGEMENT_SYSTEM") 
    connect.commit()
    connect.close()

    connect=sql.connect(host='localhost',user=userValue ,passwd=pwdValue ,database='HOTEL_MANAGEMENT_SYSTEM')
    if connect.is_connected():
        check=2
    cur=connect.cursor()

    cur.execute("create table if not exists Customer_Records(Customer_ID int primary key, Cname varchar(25) not null, RoomNo char(5) not null, PhoneNo char(10) not null, Address varchar(100) not null);")
    cur.execute("create table if not exists Room_Details(RoomNo char(5) primary key, room_type varchar(20) not null, Check_In_Date date not null, Check_Out_Date date not null, Room_Bill int not null, Food_Bill int default 0, Total_Bill int not null default 0, Payment_Status bool DEFAULT FALSE);")
    connect.commit()
    connect.close()

    if check==0:
        messagebox.showerror("Error","Login Succesful")
    elif check==1:
        messagebox.showerror("Error","Table Creation Unsuccessful")
    elif check==2:
        messagebox.showinfo("Confirm","Login and Table Creation Successful")
        x.destroy()
    file.write(f'{check}')
    file.close()
    
def mainwin():
    global username,password

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
    
    Login = Button(sqllogin, text="Login", command=lambda: sqlconnect(sqllogin))
    Login.grid(column=2,row=3)

    sqllogin.mainloop()

