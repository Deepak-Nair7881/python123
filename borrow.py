from tkinter import *
import json
from PIL import ImageTk, Image
import datetime
from datetime import date
from tkinter import messagebox
import mysql.connector

# import main

cart=[]
class borrow1:
    def __init__(self):
        self.root=None
        self.img=None
        pass
    def borrow3(self,user):

        def checkout():
            # root.destroy()
            def yes():
                cart1=json.dumps(cart)
                sql="update users set currently_borrowing=%s where email=%s;"
                values=(cart1,user)
                mycursor.execute(sql,values)
                mydb.commit()
                # sql = "select book_name,currently_borrowed from borrow"
                # mycursor.execute(sql)
                # mycursor.fetchall()
                for book_name in cart:
                    sql = "update borrow set currently_borrowed=%s where book_name=%s;"
                    values = (True, book_name)
                    mycursor.execute(sql, values)
                    sql = "update borrow set date_of_borrowing=%s where book_name=%s;"
                    date1=date.today()
                    values = (date1, book_name)
                    mycursor.execute(sql, values)
                    sql = "update borrow set date_of_returning=%s where book_name=%s;"
                    date2 = date.today() + datetime.timedelta(days=7)
                    values = (date2, book_name)
                    mycursor.execute(sql, values)
                    mydb.commit()
                root1.destroy()
            def No():
                root1.destroy()
            root1=Tk()
            root1.geometry('600x600')
            root1.title("CheckOut")
            x2=0
            y2=0
            a=Label(root1,text="Checkout details").pack()
            sql = "select book_name,link from borrow"
            mycursor.execute(sql)
            # mycursor.fetchall()
            for i in mycursor:
                if i[0] in cart:
                    self.img = ImageTk.PhotoImage(Image.open(i[1]),master=root1)
                    # label = Label(image=img)
                    # label.image=img
                    # label.place(x=100+x2, y=100+y1)
                    a = Label(root1, image=self.img)
                    a.image = self.img
                    a.place(x=100 + x2, y=100 + y2)
                    a1 = Label(root1, text=i[0]).place(x=100 + x2, y=200 + y2)
                    x2 += 100
            Button(root1, text="Yes", command=yes).pack()
            Button(root1, text="No", command=No).pack()


        mycursor=None
        root=Tk()
        root.title("BOOK")
        root.geometry('800x800')
        a = Label(root, text="Shopping list").pack()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2003",
                database="project")
            mycursor=mydb.cursor()
        except mysql.connector.Error as err:
            print(f"{err}")
        finally:
            print("success")
        sql = "select currently_borrowing from users where email=%s"
        values=(user,)
        mycursor.execute(sql,values)
        cur=mycursor.fetchall()
        cart=json.loads(cur[0][0])
        print(cart)
        sql="select book_name,link,currently_borrowed from borrow"
        mycursor.execute(sql)

        x1=0
        y1=0
        c=0
        for i in mycursor:

            def box(book_name):
                d={}
                sql = "select book_name,link,currently_borrowed from borrow"
                mycursor.execute(sql)
                for i in mycursor:
                    d[i[0]]=i[2]

                def yes():
                    if(d[book_name]==True):
                        messagebox.showinfo("Alert","Sorry not available")
                        root1.destroy()
                    else:
                        cart.append(book_name)
                        root1.destroy()
                def No():
                    root1.destroy()
                root1=Tk()
                root1.title("CONFIRMATION?")
                root1.geometry('300x300')
                a=Label(root1,text=f"Are you sure you want to add {book_name} to the cart?\nBorrow date is:{date.today()}\nReturn Date is:{date.today()+datetime.timedelta(days=7)}").pack()
                Button(root1,text="Yes",command=yes).pack()
                Button(root1,text="No",command=No).pack()
                root1.mainloop()
                pass
            self.img = ImageTk.PhotoImage(Image.open(i[1]),root)

            # label = Label(image=img)
            # label.image=img
            # label.place(x=100+x1, y=100+y1)
            button=Button(root,image=self.img,command=lambda book=i[0]: box(book))
            button.image=self.img
            button.place(x=100 + x1, y=100 + y1)
            a = Label(root, text=i[0]).place(x=100+x1,y=200+y1)
            x1+=100
            c+=1
            if(c%6==0):
                print("\n")
                y1+=200
                x1=0

        self.img = ImageTk.PhotoImage(Image.open("proceed-to-pay-button-216653832.jpg"))
        button1 = Button(root, image=self.img,command=checkout)
        button1.image=self.img
        button1.place(x=550,y=600)
        # button2=Button(root,text="Back",command=lambda root=root:main.main_page(root,user))
        # button2.place(x=0,y=0)
        root.mainloop()

        pass