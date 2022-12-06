import os
import sys
current=os.path.dirname(os.path.realpath(__file__))
parent=os.path.dirname(current)
sys.path.append(parent)
import connector

class Customer(object):
    def __init__(self):
        self.customer_id=0
        self.customer_name=""
        self.phno=""
        self.address=""
        self.roomno=""
        self.checkin=""
        self.checkout=""
        self.roombill=0
        self.foodbill=0
        self.totalbill=0
        self.roomtype=""

    def customer_load(self,custid):
        sqlObj=connector.SQLCursor()
        sqlObj.sqlconnect()
        sqlObj.sqlcursor.execute("SELECT Customer_ID, CName, PhoneNo, Address, customer_records.RoomNo, Room_Type, Check_In_Date, Check_Out_Date, Room_Bill, Food_Bill, Total_Bill FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo AND customer_id=%s;",(custid,))
        custList=sqlObj.sqlcursor.fetchall()[0]
        sqlObj.connect.close()

        self.customer_id=custList[0]
        self.customer_name=custList[1]
        self.phno=custList[2]
        self.address=custList[3]
        self.roomno=custList[4]
        self.roomtype=custList[5]
        self.checkin=custList[6]
        self.checkout=custList[7]
        self.roombill=custList[8]
        self.foodbill=custList[9]
        self.totalbill=custList[10]

    def customer_details_record(self):   
        return (self.customer_id,self.customer_name,self.roomno,self.phno,self.address)
    
    def room_details_record(self):
        return (self.roomno,self.roomtype, self.checkin,self.checkout,self.roombill)
    
    def customer_update_sql(self):
        sqlobj=connector.SQLCursor()
        sqlobj.sqlconnect()
        sqlobj.initialCustomer_Details(self.customer_details_record())
        sqlobj.connect.close()

    def room_update_sql(self):
        sqlobj=connector.SQLCursor()
        sqlobj.sqlconnect()
        sqlobj.initialRoom_Details(self.room_details_record())
        sqlobj.connect.close()

    def customer_update_foodbill(self,food_bill,room_no):
        sqlobj=connector.SQLCursor()
        sqlobj.sqlconnect()
        Update="UPDATE room_details SET food_bill=%s WHERE roomno=%s"
        sqlobj.sqlcursor.execute(Update,(food_bill,room_no,))
        sqlobj.connect.commit()
        sqlobj.connect.close()

    def customer_update_paymentstatus(self,paymentstatus,room_no):
        sqlobj=connector.SQLCursor()
        sqlobj.sqlconnect()
        Update="UPDATE room_details SET payment_status=%s WHERE roomno=%s"
        sqlobj.sqlcursor.execute(Update,(paymentstatus,room_no,))
        sqlobj.connect.commit()
        sqlobj.connect.close()