from tkinter import *
from Customer import CustomerClass
import connector

customer=CustomerClass.Customer()
customer.customer_load
customer.totalbill=customer.foodbill+customer.roombill

def destroy():
    MainWin.destroy()

def update():
    sqlobj=connector.SQLCursor()
    sqlobj.sqlconnect()
    RInsert="UPDATE room_details SET food_bill=%s, total_bill=%s where RoomNo=%s"
    sqlobj.sqlcursor.execute(RInsert, (customer.foodbill,customer.totalbill,customer.roomno))
    sqlobj.connect.commit()
    sqlobj.connect.close()

def showBill():
    BillWindow=Tk()
    BillWindow.title("BILL")
    
    TitleMsg=Label(BillWindow,text="HOTEL PHOENIX",font="Impact 15 underline")
    TitleMsg.pack(pady=2)

    subTitleMsg=Label(BillWindow,text="BILL",font="Impact 15 underline")
    subTitleMsg.pack(pady=2)

    BillString=f"Name>> {customer.customer_name} \nPhone No.>> {customer.phno} \nAddress>> {customer.address} \nCheck-In>> {customer.checkin} \
        \nCheck-Out>> {customer.checkout} \nRoom Type>> {customer.roomtype} \nRoom Charges>> {customer.roombill} \nRestaurant Charges>> {customer.foodbill} \
        \n--------------------------------------- \nAmount>> {customer.totalbill} \n--------------------------------------- \nThank You \nVisit Again!"

    Bill=Label(BillWindow,text=BillString)
    Bill.pack(pady=2)

    backButton=Button(BillWindow,text="Back",command= lambda: [BillWindow.destroy(),update()])
    backButton.pack()

    BillWindow.mainloop()

def PaymentButton():
    global MainWin

    MainWin=Tk()
    MainWin.title("Payment")
    MainWin.geometry('300x150')

    TitleMsg=Label(MainWin,text="PAYMENT",font="Impact 15 underline")
    TitleMsg.pack(pady=2)

    holdFrame=Frame(MainWin)
    holdFrame.pack(pady=2)
    
    MoP=[
        "Credit/Debit Card", "PayTM/PhonePe", "Using UPI", "Cash"
    ]

    clicked=StringVar()
    clicked.set("Credit/Debit Card")

    MoPLabel=Label(holdFrame, text="Mode of Payment>>")
    MoPLabel.grid(row=0,column=0,padx=2,pady=2)
    MoPEntry=OptionMenu(holdFrame, clicked, *MoP)
    MoPEntry.grid(row=0, column=1,padx=2,pady=2)

    AmountLabel=Label(holdFrame, text=f"Amount>> {customer.totalbill}")
    AmountLabel.grid(row=1, column=1,padx=2, pady=2)
    
    payButton=Button(holdFrame, text="Pay for Phoenix", command=lambda: showBill())
    payButton.grid(row=1,column=1,padx=2,pady=2)

    backButton=Button(MainWin, text="Back", command=lambda: destroy())
    backButton.pack(pady=10)

    MainWin.mainloop()

