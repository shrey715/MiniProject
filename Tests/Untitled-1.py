from tkinter import *
from PIL import ImageTk, Image

test=Tk()
frame=Frame(test)

dict={1:frame}

Bev=Image.open("Images\Beverages.jpeg")
imgBev=ImageTk.PhotoImage(master=frame,image=Bev)
lab1=Label(frame,image=imgBev)
lab1.image=imgBev
lab1.pack()

dict[1].pack()
test.mainloop()