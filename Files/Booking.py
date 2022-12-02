from tkinter import *
from tkcalendar import DateEntry
from datetime import date
import mysql.connector as mysql

with open("Variables\SQLUsername.txt","r") as file:
    userValue=file.readline()

with open("Variables\SQLPassword.txt","r") as file:
    pwdValue=file.readline()

f1=open("Variables\CustomerClass\CustomerName.txt","w")
f2=open("Variables\CustomerClass\CustomerPhoneNumber.txt","w")
f3=open("Variables\CustomerClass\CustomerAddress.txt","w")
f4=open("Variables\CustomerClass\CustomerCheckInDate.txt","w")
f5=open("Variables\CustomerClass\CustomerCheckOutDate.txt","w")
f6=open("Variables\CustomerClass\CustomerRoom.txt","w")
f7=open("Variables\CustomerClass\CustomerRoomBill.txt","w")
f8=open("Variables\CustomerClass\CustomerRoomNo.txt","w")

def confirmation():
    f1.write(str(CName.get()))
    f2.write(str(PhNo.get()))
    f3.write(str(Addr.get()))
    f4.write(str(ChkInDate.get()))
    f5.write(str(ChkOutDate.get()))
    f6.write(str(clicked.get()))

def BookingButton():
    global CName, PhNo, Addr, ChkInDate, ChkOutDate, clicked
    
    BookingRooms = Tk()
    BookingRooms.title("Booking")
    BookingRooms.geometry("500x500")

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

    #Note= add check for diff chk in chk out dates

    Rooms=["Standard Non-AC",
         "Standard AC",
         "3-Bed Non-AC",
          "3-Bed AC"]

    clicked=StringVar()
    clicked.set("Standard Non-AC")

    RoomTypeLabel=Label(BookingRooms, text="Enter Room Type>> ")
    RoomTypeLabel.grid(row=5, column=0, pady=5)
    RoomType=OptionMenu(BookingRooms, clicked, *Rooms)
    RoomType.grid(row=5, column=1, pady=5)

    ConfirmButton=Button(BookingRooms, text="Click to Book", command=confirmation)
    ConfirmButton.grid(row=6,column=1, pady=5)

    BookingRooms.mainloop()