from tkinter import *
from Files import initialisation

file=open("firstruncheck.txt","r+")
check='0' in file.read()
file.close()

if check:
    file=open("firstruncheck.txt","w")
    file.write('1')
    file.close()
    initialisation.mainwin()

HomePageWin= Tk()
