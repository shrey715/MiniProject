from tkinter import *
from Customer import CustomerClass
import connector
from tkinter import messagebox

def destroy():
    MainWin.destroy()

def update():
    sqlobj=connector.SQLCursor()
    sqlobj.sqlconnect()
    RInsert="UPDATE room_details SET total_bill=%s,payment_status=True where RoomNo=%s"
    sqlobj.sqlcursor.execute(RInsert, (customer.totalbill,customer.roomno,))
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

def on_click():
    global customer
    sqlObj=connector.SQLCursor()
    sqlObj.sqlconnect()
    sqlObj.sqlcursor.execute("SELECT Customer_ID FROM customer_records;")
    li=sqlObj.sqlcursor.fetchall()
    sqlObj.connect.close()

    if (int(custID.get()),) not in li:
        messagebox.showerror("Invalid Customer ID", "Customer ID entered is invalid")
        return None

    customer=CustomerClass.Customer()
    customer.customer_load(int(custID.get()))

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

def PaymentButton():
    global MainWin, custID

    MainWin=Tk()
    MainWin.title("Payment")
    MainWin.geometry('300x300+500+100')

    TitleMsg=Label(MainWin,text="PAYMENT",font="Impact 15 underline")
    TitleMsg.pack(pady=2)

    custFrame=Frame(MainWin)
    custFrame.pack()

    custIDLabel=Label(custFrame, text="Customer ID>>")
    custIDLabel.grid(row=0,column=0,padx=2,pady=2)

    custID=Entry(custFrame,width=10)
    custID.grid(row=0, column=1,padx=2,pady=2)

    okButton=Button(custFrame, text="Ok", command=lambda: on_click())
    okButton.grid(row=1,column=1,padx=2,pady=2)

    backButton=Button(MainWin, text="Back", command=lambda: destroy())
    backButton.pack(pady=10,side=BOTTOM)

    MainWin.mainloop()

