from tkinter import *
import borrow
import return1
import profile
import review
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import datetime
import mysql.connector
from tkinter import messagebox
c=0
class main_page2:
    def __init__(self):
        pass
    def main_page(self,user,root):
        root.destroy()
        def borrow2():
            root.destroy()
            connect2.borrow3(user)
        # main_page()
        def return2():
            root.destroy()
            connect4.return3(user)
            pass
        def profile2():
            root.destroy()
            connect5.profile2(user)
            pass
        def review2():
            root.destroy()
            connect8.review2(user)
            pass
        connect=borrow
        connect2=connect.borrow1()
        connect3 = return1
        connect4 = connect3.return2()
        connect6=profile
        connect5 = connect6.profile1()
        connect7 = review
        connect8 = connect7.review1()
        root = Tk()
        root.title("BOOK")
        root.geometry('800x800')
        a = Label(root, text="MENU").pack()
        Button(root, text="Borrow", command=borrow2).place(x=400, y=200)
        Button(root, text="Return", command=return2).place(x=400, y=300)
        Button(root, text="Profile", command=profile2).place(x=400, y=400)
        Button(root, text="Review", command=review2).place(x=400, y=500)


        root.mainloop()