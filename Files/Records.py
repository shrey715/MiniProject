from tkinter import *
from connector import *
from pandastable import Table
from pandas import DataFrame

def getAll():
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID,  PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo;")
    rows=sqlobj.sqlcursor.fetchall()
    df=DataFrame(data=rows,index=range(1,len(rows)+1),columns=column)
    recordsTable.model.df=df
    recordsTable.redraw()

def searchGo():
    custid=searchEntry.get()
    sqlobj.sqlcursor.execute("SELECT Cname, Customer_ID, PhoneNo, Address, Check_In_Date, Check_Out_Date, Room_Type, Room_Bill FROM customer_records, room_details WHERE customer_records.RoomNo=room_details.RoomNo AND customer_id=%s;",(custid,))
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
    MainWin.maxsize(1000,460)
    MainWin.minsize(1000,460)

    TitleMsg=Label(MainWin,text="HOTEL PHOENIX - RECORDS",font="Impact 15 underline")
    TitleMsg.pack(pady=2)

    OptionFrame=Frame(MainWin)
    OptionFrame.pack(pady=2)

    Button1=Button(OptionFrame, text="All", command=lambda: getAll())
    Button1.grid(row=0,column=0,padx=8,pady=2)

    def but2():
        global searchEntry
        searchLabel=Label(OptionFrame, text="Enter CustomerID>>")
        searchLabel.grid(row=1,column=0,padx=8,pady=2)

        searchEntry=Entry(OptionFrame, width=10)
        searchEntry.grid(row=1,column=1,padx=8,pady=2)

        goButton=Button(OptionFrame, text="Go", command=lambda: searchGo())
        goButton.grid(row=1,column=2,padx=8,pady=2)

    Button2=Button(OptionFrame,text="Search", command=lambda: but2())
    Button2. grid(row=0, column=1, padx=8, pady=2)
    
    TableFrame=Frame(MainWin)
    TableFrame.pack()

    column=['Name','Customer ID','Phone No','Address','Check-In Date', 'Check-Out Date', 'Room Type', 'Price']
    defaultdf=DataFrame(data=[],index=[0],columns=column)
    recordsTable=Table(TableFrame,dataframe=defaultdf,width=900,cellwidth=112.5)
    recordsTable.show()

    backButton=Button(MainWin, text="Back", command=lambda: destroy())
    backButton.pack(pady=10)

    MainWin.mainloop()

