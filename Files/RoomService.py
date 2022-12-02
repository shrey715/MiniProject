from tkinter import *
from PIL import ImageTk, Image

def destroy():
    MainWin.destroy()

def MenuCard():
    global MainWin
    MainWin=Tk()
    MainWin.title("Menu Card")

    MainWin.geometry("500x700")
    MainWin.minsize(500,700)
    MainWin.maxsize(500,700)
    
    TitleMsg=Label(MainWin, text="HOTEL PHOENIX\nMENU CARD", font="Impact 15 underline")
    TitleMsg.pack()

    MenuCardFrame=Frame(MainWin)
    MenuCardFrame.pack()

    ele={ 
    }

    for c in range(1,3):
        for r in range(1,):
        

    BackButton=Button(MainWin, text="Back", command= lambda:destroy())
    BackButton.pack()

    MainWin.mainloop()

MenuCard()