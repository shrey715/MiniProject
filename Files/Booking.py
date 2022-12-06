from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from Customer import CustomerClass
from random import randrange
import connector

with open("Variables\SQLUsername.txt","r") as file:
    userValue=file.readline()

with open("Variables\SQLPassword.txt","r") as file:
    pwdValue=file.readline()

def confirmcheck():
    if len(str(PhNo.get()).strip())==10 and ChkInDate.get_date()<ChkOutDate.get_date():
        gen()
        confirmation()
    if len(str(PhNo.get()).strip())!=10:
        messagebox.showerror("Error","Invalid phone number")
    if not ChkInDate.get_date()<ChkOutDate.get_date():
        messagebox.showerror("Error","Invalid check-in and check-out dates selected")

def confirmation():
    global customer
    customer=CustomerClass.Customer()
    customer.customer_name=CName.get()
    customer.customer_id=custid
    customer.phno=PhNo.get()
    customer.address=Addr.get()
    customer.checkin=ChkInDate.get().replace("/","-")
    customer.checkout=ChkOutDate.get().replace("/","-")
    customer.roomtype=room.get()

    if room.get()==Rooms[0]:
        rmno=f"D{rno}"
    elif room.get()==Rooms[1]:
        rmno=f"C{rno}"
    elif room.get()==Rooms[2]:
        rmno=f"B{rno}"
    elif room.get()==Rooms[3]:
        rmno=f"A{rno}"
    customer.roomno=rmno

    customer.roombill=RoomBill()
    customer.foodbill=0
    customer.totalbill=0

    customer.customer_update_sql()
    customer.room_update_sql()    

def gen():
    global custid, rno

    sqlobj=connector.SQLCursor()
    sqlobj.sqlconnect()
    sqlobj.sqlcursor.execute("SELECT RoomNo from Room_Details;")
    RoomNoList=sqlobj.sqlcursor.fetchall()
    sqlobj.sqlcursor.execute("SELECT Customer_ID from customer_records;")
    CustIDList=sqlobj.sqlcursor.fetchall()
    sqlobj.connect.close()

    rno=randrange(1,10000)
    custid=randrange(80000)+100000

    while rno in RoomNoList or custid in CustIDList:
        rno=randrange(899)+3000
        custid=randrange(80000)+100000

def RoomBill():
    days=(ChkOutDate.get_date()-ChkInDate.get_date()).days
    
    if room.get()==Rooms[0]:
        return days*3500
    elif room.get()==Rooms[1]:
        return days*4000
    elif room.get()==Rooms[2]:
        return days*4500
    elif room.get()==Rooms[3]:
        return days*5000

def destroy():
    BookingRooms.destroy()

def detailsdisplay():
    DetailsString=f"Name>>{customer.customer_name}\nPhoneNo>>{customer.phno}\nCustomerID>>{customer.customer_id}\nRoomNo>>{customer.roomno}"
    messagebox.showinfo("Booking Complete",DetailsString)

def BookingButton():
    global BookingRooms, CName, PhNo, Addr, ChkInDate, ChkOutDate, room, Rooms

    BookingRooms = Tk()
    BookingRooms.title("Booking")
    BookingRooms.geometry("500x300")

    NameLabel=Label(BookingRooms, text="Enter Name>> ")
    NameLabel.grid(row=0, column=0, pady=5)
    CName=Entry(BookingRooms, width=40)
    CName.grid(row=0,column=1, pady=5)

    PhoneNumLabel=Label(BookingRooms, text="Enter Phone Number>> ")
    PhoneNumLabel.grid(row=1,column=0, pady=5)
    PhNo=Entry(BookingRooms, width=40)
    PhNo.grid(row=1,column=1, pady=5)

    AdrLabel=Label(BookingRooms, text="Enter Address>> ")
    AdrLabel.grid(row=2,column=0, pady=5)
    Addr=Entry(BookingRooms,width = 40)
    Addr.grid(row=2,column=1, pady=5)

    ChkInLabel=Label(BookingRooms, text="Enter your check-in date>> ")
    ChkInLabel.grid(row=3,column=0, pady=5)
    ChkInDate=DateEntry(BookingRooms, selectmode='day', date_pattern ='yyyy/mm/dd')
    ChkInDate.grid(row=3,column=1, pady=5)

    ChkOutLabel=Label(BookingRooms, text="Enter your check-out date>> ")
    ChkOutLabel.grid(row=4,column=0, pady=5)
    ChkOutDate=DateEntry(BookingRooms, selectmode='day', date_pattern ='yyyy/mm/dd')
    ChkOutDate.grid(row=4,column=1, pady=5)

    Rooms=["Standard Non-AC",
         "Standard AC",
         "3-Bed Non-AC",
          "3-Bed AC"]

    room=StringVar()
    room.set("Standard Non-AC")
    
    RoomTypeLabel=Label(BookingRooms, text="Enter Room Type>> ")
    RoomTypeLabel.grid(row=5, column=0, pady=5)
    RoomType=OptionMenu(BookingRooms, room, *Rooms)
    RoomType.grid(row=5, column=1, pady=5)

    ConfirmButton=Button(BookingRooms, text="Click to Book", command=lambda: [confirmcheck(),detailsdisplay(),destroy()])
    ConfirmButton.grid(row=6,column=1, pady=5)

    BackButton=Button(BookingRooms, text="Back", command=lambda:destroy())
    BackButton.grid(row=7,column=1,pady=5)

    BookingRooms.mainloop()

