from tkinter import *
from Files import initialisation,Booking,RoomInfo,RoomService,Payment,Records
import pickle


file=open("checks.dat","r+")
check='0' in file.read()
file.close()

if check:
    
    initialisation.mainwin()

HomePageWin= Tk()
HomePageWin.title("Home Page")

WelcomeMsg=Label(HomePageWin, text="WELCOME  TO  HOTEL  PHOENIX",font="Broadway 18")
WelcomeMsg.pack()

#def but1():
    
#def but2():

#def but3():

#def but4():

#def but5():

def but6():
    HomePageWin.destroy()

Button1=Button(HomePageWin, text="BOOKING",width=25)
Button2=Button(HomePageWin, text="ROOM INFO",width=25)
Button3=Button(HomePageWin, text="ROOM SERVICE(MENU CARD)",width=25)
Button4=Button(HomePageWin, text="PAYMENT",width=25)
Button5=Button(HomePageWin, text="RECORDS",width=25)
Button6=Button(HomePageWin, text="EXIT",width=25)

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()

HomePageWin.mainloop()