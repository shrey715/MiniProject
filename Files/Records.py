from tkinter import *
from connector import *
from pandastable import Table
from pandas import DataFrame

def getAll():
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID, PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill, Total_Bill, Payment_Status FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo;")
    rows=sqlobj.sqlcursor.fetchall()
    df=DataFrame(data=rows,index=range(1,len(rows)+1),columns=column)
    recordsTable.model.df=df
    recordsTable.redraw()

def searchGo():
    custid=searchEntry.get()
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID, PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill, Total_Bill, Payment_Status FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo AND customer_id=%s;",(custid,))
    rows=sqlobj.sqlcursor.fetchall()
    df=DataFrame(data=rows,index=range(1,len(rows)+1),columns=column)
    recordsTable.model.df=df
    recordsTable.redraw()

def notPaid():
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID, PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill, Total_Bill, Payment_Status FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo AND payment_status=%s;",(False,))
    rows=sqlobj.sqlcursor.fetchall()
    df=DataFrame(data=rows,index=range(1,len(rows)+1),columns=column)
    recordsTable.model.df=df
    recordsTable.redraw()

def Paid():
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID, PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill, Total_Bill, Payment_Status FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo AND payment_status=%s;",(True,))
    rows=sqlobj.sqlcursor.fetchall()
    df=DataFrame(data=rows,index=range(1,len(rows)+1),columns=column)
    recordsTable.model.df=df
    recordsTable.redraw()

def destroy():
    sqlobj.connect.close()
    MainWin.destroy()

def RecordsButton():
    global sqlobj, MainWin, recordsTable, column
    sqlobj=SQLCursor()
    sqlobj.sqlconnect()
    
    MainWin=Tk()
    MainWin.title("Records")
    MainWin.geometry("1050x460+500+100")
    MainWin.maxsize(1050,460)
    MainWin.minsize(1050,460)

    TitleMsg=Label(MainWin,text="HOTEL PHOENIX - RECORDS",font="Impact 15 underline")
    TitleMsg.pack(pady=2)

    OptionFrame=Frame(MainWin)
    OptionFrame.pack(pady=2)

    Button1=Button(OptionFrame, text="All", command=lambda: getAll())
    Button1.grid(row=0,column=0,padx=8,pady=2)
    
    Button2=Button(OptionFrame, text="Paid", command=lambda: Paid())
    Button2.grid(row=0,column=1,padx=8,pady=2)
    
    Button3=Button(OptionFrame, text="Not Paid", command=lambda: notPaid())
    Button3.grid(row=0,column=2,padx=8,pady=2)

    def but2():
        global searchEntry
        searchLabel=Label(OptionFrame, text="CustomerID>>")
        searchLabel.grid(row=1,column=0,padx=8,pady=2)

        searchEntry=Entry(OptionFrame, width=10)
        searchEntry.grid(row=1,column=1,padx=8,pady=2)

        goButton=Button(OptionFrame, text="Go", command=lambda: searchGo())
        goButton.grid(row=1,column=2,padx=8,pady=2)

    Button4=Button(OptionFrame,text="Search", command=lambda: but2())
    Button4. grid(row=0, column=3, padx=8, pady=2)
    
    TableFrame=Frame(MainWin)
    TableFrame.pack()

    column=['Name','Customer ID','Phone No','Address','Check-In Date', 'Check-Out Date', 'Room Type', 'Room Bill','Total Bill','Payment Status']
    defaultdf=DataFrame(data=[],index=[0],columns=column)
    recordsTable=Table(TableFrame,dataframe=defaultdf,width=1000,cellwidth=100)
    recordsTable.show()

    backButton=Button(MainWin, text="Back", command=lambda: destroy())
    backButton.pack(pady=10)

    MainWin.mainloop()


