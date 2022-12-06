from tkinter import *
import sys
import os
sys.path.append(os.path.dirname(__file__)+'\Files')
from Files import initialisation,RoomInfo,Booking,RoomService,Payment,Records,Customer

file=open("Variables\InitialisationCheck.txt","r")
check=int(file.readlines()[0])
file.close()

if check==0:
    initialisation.mainwin()

HomePageWin= Tk()
HomePageWin.title("Home Page")
HomePageWin.geometry("500x300+500+100")

WelcomeMsg=Label(HomePageWin, text="WELCOME  TO  HOTEL  PHOENIX",font="Broadway 18")
WelcomeMsg.pack(pady=10)

def but1():
    Booking.BookingButton()

def but2():
    RoomInfo.RoomsInfoButton()

def but3():
    RoomService.RoomServiceButton()

def but4():
    Payment.PaymentButton()

def but5():
    Records.RecordsButton()

def but6():
    HomePageWin.destroy()

Button1=Button(HomePageWin, text="BOOKING",width=25, command= lambda: but1())
Button2=Button(HomePageWin, text="ROOM INFO",width=25,command=lambda: but2())
Button3=Button(HomePageWin, text="ROOM SERVICE(MENU CARD)",width=25, command= lambda:but3())
Button4=Button(HomePageWin, text="PAYMENT",width=25, command= lambda: but4())
Button5=Button(HomePageWin, text="RECORDS",width=25, command= lambda: but5())
Button6=Button(HomePageWin, text="EXIT",width=25,command=lambda: but6())

Button1.pack(pady=5)
Button2.pack(pady=5)
Button3.pack(pady=5)
Button4.pack(pady=5)
Button5.pack(pady=5)
Button6.pack(pady=5)

HomePageWin.mainloop()