from tkinter import *
from PIL import ImageTk, Image
from Customer import CustomerClass
from pickle import *

def onCall():
    global r
    with open("Files\Customer\customer.dat","rb") as file:
        li=load(file)
        r=load[9]

def destroyCard():
    MainWin.destroy()

def MenuCard():
    global MainWin
    MainWin=Tk()
    MainWin.title("Menu Card")

    MainWin.geometry("500x700")
    MainWin.maxsize(500,700)
    MainWin.minsize(500,700)

    TitleMsg=Label(MainWin, text="HOTEL PHOENIX\nMENU CARD", font="Impact 15 underline")
    TitleMsg.pack()

    MenuCardFrame=Frame(MainWin)
    MenuCardFrame.pack()
    
    MenuCardImg=ImageTk.PhotoImage(image=Image.open("Images\MenuCard1.jpeg"),master=MenuCardFrame)
    imgLabel=Label(MenuCardFrame,image=MenuCardImg)
    imgLabel.image=MenuCardImg
    imgLabel.pack()

    BackButton=Button(MainWin, text="Back", command= lambda:destroyCard())
    BackButton.pack()

    MainWin.mainloop()

def onclick_order():
    global r
    ch=int(OrderEntry.get())
    if ch==1 or ch==31 or ch==32:
        rs=20
        r=r+rs
    elif ch<=4 and ch>=2:   
        rs=25
        r=r+rs
    elif ch<=6 and ch>=5:
        rs=30
        r=r+rs
    elif ch<=8 and ch>=7:   
        rs=50
        r=r+rs
    elif ch<=10 and ch>=9:
        rs=70
        r=r+rs
    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
        rs=110
        r=r+rs
    elif ch<=19 and ch>=18:
        rs=120
        r=r+rs
    elif (ch<=26 and ch>=20) or ch==42:
        rs=140
        r=r+rs
    elif ch<=28 and ch>=27:
        rs=150
        r=r+rs
    elif ch<=30 and ch>=29:
        rs=15
        r=r+rs
    elif ch==33 or ch==34:
        rs=90
        r=r+rs
    elif ch==37:
        rs=100
        r=r+rs
    elif ch<=41 and ch>=39:
        rs=130
        r=r+rs
    elif ch<=46 and ch>=43:
        rs=60
        r=r+rs
    else:
        DisplayLabel.text="WRONG CHOICE!"

def onclick_totalbill():
    DisplayLabel=Label(DisplayFrame,text=f"Total bill is {r}")
    customer=CustomerClass.Customer()
    customer.customer_load()
    customer.foodbill=r
    customer.customer_update()

def onclick_cancel():
    global r
    ch=int(OrderEntry.get())
    if ch==1 or ch==31 or ch==32:
        rs=20
        r=r-rs
    elif ch<=4 and ch>=2:   
        rs=25
        r=r-rs
    elif ch<=6 and ch>=5:
        rs=30
        r=r-rs
    elif ch<=8 and ch>=7:   
        rs=50
        r=r-rs
    elif ch<=10 and ch>=9:
        rs=70
        r=r-rs
    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
        rs=110
        r=r-rs
    elif ch<=19 and ch>=18:
        rs=120
        r=r-rs
    elif (ch<=26 and ch>=20) or ch==42:
        rs=140
        r=r-rs
    elif ch<=28 and ch>=27:
        rs=150
        r=r-rs
    elif ch<=30 and ch>=29:
        rs=15
        r=r-rs
    elif ch==33 or ch==34:
        rs=90
        r=r-rs
    elif ch==37:
        rs=100
        r=r-rs
    elif ch<=41 and ch>=39:
        rs=130
        r=r-rs
    elif ch<=46 and ch>=43:
        rs=60
        r=r-rs
    else:
        DisplayLabel.text="WRONG CHOICE!"

def RoomServiceButton():
    onCall()
    global OrderEntry,DisplayFrame,DisplayLabel

    RoomServices=Tk()
    RoomServices.title("Room Service")
    RoomServices.geometry("300x300")

    TitleMsg=Label(RoomServices, text="ROOM SERVICE", font="Impact 15 underline")
    TitleMsg.pack(pady=10)
    
    MCButton=Button(RoomServices, text="Open Menu Card", command=lambda: MenuCard())
    MCButton.pack()

    OrderFrame=Frame(RoomServices)
    OrderFrame.pack()

    OrderLabel=Label(OrderFrame, text="Enter the serial number of the item>> ")
    OrderEntry=Entry(OrderFrame, width=10)
    OrderLabel.grid(row=0,column=0,padx=2,pady=2)
    OrderEntry.grid(row=0,column=1,padx=2,pady=2)
    OrderButton=Button(OrderFrame, text="Order", command=lambda: onclick_order())
    OrderButton.grid(row=1,column=0,padx=5,pady=2)
    CancelButton=Button(OrderFrame, text="Cancel", command=lambda: onclick_cancel())
    CancelButton.grid(row=1,column=1,padx=5,pady=2)

    TotalBillButton=Button(OrderFrame, text="Total Bill", command=lambda: onclick_totalbill())
    TotalBillButton.grid(row=2,column=0,padx=5,pady=2)

    DisplayFrame=Frame(RoomServices)
    DisplayFrame.pack()
    DisplayLabel=Label(DisplayFrame)
    DisplayLabel.pack()

    RoomServices.mainloop()
