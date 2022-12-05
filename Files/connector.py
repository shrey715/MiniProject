import mysql.connector as sql
from tkinter import messagebox

class SQLCursor(object): 
    def __init__(self):
        self.connect=0

    def sqlconnect(self):
        with open("Variables\SQLUsername.txt","r") as file:
            userv=file.readline()

        with open("Variables\SQLPassword.txt","r") as file:
            pwd=file.readline()

        self.connect=sql.connect(host='localhost',user=userv ,passwd=pwd ,database='HOTEL_MANAGEMENT_SYSTEM')
        if not self.connect.is_connected():
            messagebox.showerror("Connection Error", "MySQLConnection failed, check username and password.")
        self.sqlcursor=self.connect.cursor()

    def initialCustomer_Details(self,custDetails):
        CInsert="INSERT INTO Customer_Records (Customer_ID, Cname, RoomNo, PhoneNo, Address)values(%s,%s,%s,%s,%s)"
        self.sqlcursor.execute(CInsert,custDetails)
        self.connect.commit()
    
    def initialRoom_Details(self,roomDetails):
        RInsert="INSERT INTO Room_Details (RoomNo, room_type, Check_In_Date, Check_Out_Date, Room_Bill)values(%s,%s,%s,%s,%s)"
        self.sqlcursor.execute(RInsert,roomDetails)
        self.connect.commit()