from tkinter import *

def destroy():
    RoomsInfo.destroy()

def RoomsInfoButton():
    global RoomsInfo
    RoomsInfo=Tk()
    RoomsInfo.title("Room Information")
    RoomsInfo.geometry("1000x500+500+100")

    TitleMsg=Label(RoomsInfo, text="HOTEL ROOMS INFO", font="Impact 15 underline")
    TitleMsg.pack(pady=10)

    tableGrid=Frame(RoomsInfo,bg="#a0b1b9")
    tableGrid.pack()

    TableContent={
        (0,1):"ROOMS" , (0,2):"AMENTITIES",(0,3):"PRICES",
        (1,1):"STANDARD NON-AC" , (1,2):"1 Double Bed, Television, Telephone, \nDouble-Door Cupboard, 1 Coffee table with 2 sofa, \nBalcony and attached washroom with hot/cold water." , (1,3):"Rs. 3500",
        (2,1):"STANDARD AC" , (2,2):"1 Double Bed, Television, Telephone, \nDouble-Door Cupboard, 1 Coffee table with 2 sofa, Balcony \nand attached washroom with hot/cold water + Window/Split AC" , (2,3):"Rs. 4000",
        (3,1):"3-BED NON-AC" , (3,2):"1 Double Bed + 1 Single Bed, Television, Telephone, \na Triple-Door Cupboard, 1 Coffee table with 2 sofa, \n1 Side table, Balcony with an Accent table with 2 Chair \nand an attached washroom with hot/cold water." , (3,3):"Rs. 4500",
        (4,1):"3-BED AC" , (4,2):"1 Double Bed + 1 Single Bed, Television, Telephone, \na Triple-Door Cupboard, 1 Coffee table with 2 sofa, \n1 Side table, Balcony with an Accent table with 2 Chair \nand an attached washroom with hot/cold water + Window/Split AC" , (4,3):"Rs. 5000"
        }

    for r in range(0,5):
        for c in range(1,4):
            roomGrid=Frame(tableGrid, relief=RAISED, borderwidth=2)
            roomGrid.grid(row=r,column=c,padx=5,pady=5)

            w=20
            if c==2:
                w=70

            eleGrid=Label(roomGrid, text=TableContent[(r,c)], width=w, font="Optima 10")

            if c==1 or r==0:
                eleGrid.config(bg="#8e8e8e",font="Optima 10 bold")

            eleGrid.pack()

    backButton=Button(RoomsInfo,text="Back",command=lambda: destroy())
    backButton.pack(pady=10)

    TitleMsg.mainloop()

