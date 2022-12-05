
from pickle import *

f=open("Files\Customer\customer.dat","rb")
li=load(f)
print(li)
"""
from tkinter import *
from tkcalendar import DateEntry

tk=Tk()
d1=DateEntry(tk, selectmode='day', date_pattern ='yyyy/mm/dd')
d2=DateEntry(tk, selectmode='day', date_pattern ='yyyy/mm/dd')
d1.pack()
d2.pack()
days=d2.get_date()- d1.get_date()

def but():
    print(days)

button=Button(tk, text="chk",command=but)
button.pack()
tk.mainloop()
"""