from tkinter import *
from tkcalendar import DateEntry
from datetime import date
import mysql.connector as mysql

with open("Variables\SQLUsername.txt","r") as file:
    userValue=file.readline()

with open("Variables\SQLPassword.txt","r") as file:
    pwdValue=file.readline()

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

Rooms=["Standard Non-AC >> Rs.3500",
         "Standard AC >> Rs.4000",
         "3-Bed Non-AC >> Rs.4500",
          "3-Bed AC >> Rs.5000"]

clicked=StringVar()
clicked.set("Standard Non-AC")

RoomTypeLabel=Label(BookingRooms, text="Enter Room Type>> ")
RoomTypeLabel.grid(row=5, column=0, pady=5)
RoomType=OptionMenu(BookingRooms, clicked, *Rooms)
RoomType.grid(row=5, column=1, pady=5)

def confirmation():
    connect=mysql.connect(host='localhost',user=userValue ,passwd=pwdValue ,database='HOTEL_MANAGEMENT_SYSTEM')
    if connect.is_connected():
        print("Successful")

ConfirmButton=Button(BookingRooms, text="Click to Book", command=confirmation)
ConfirmButton.grid(row=6,column=1, pady=5)

BookingRooms.mainloop()