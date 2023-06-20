from tkinter import *
import json
from PIL import ImageTk, Image
import datetime
from datetime import date
from tkinter import messagebox
import mysql.connector
class review1:
    def __init__(self):
        self.root=None
        self.text_entry = None
        pass
    def review2(self,user):
        def enter(book):
            rev=self.text_entry.get("1.0", "end-1c")
            if len(rev)>650:
                messagebox.showinfo(title="Alert",message="Too many characters")
            mycursor = None
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="2003",
                    database="project"
                )
                mycursor = mydb.cursor()
            except mysql.connector.Error as err:
                print(f"{err}")
                messagebox.showerror("Error", "Failed to connect to the database.")
                root.destroy()
                return
            sql="insert into review values(%s,%s,%s)"
            values=(book,user,rev)
            mycursor.execute(sql,values)
            mydb.commit()
            mydb.close()


        def display(book):
            root2=Tk()
            root2.geometry('500x500')

            mycursor = None
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="2003",
                    database="project"
                )
                mycursor = mydb.cursor()
            except mysql.connector.Error as err:
                print(f"{err}")
                messagebox.showerror("Error", "Failed to connect to the database.")
                root.destroy()
                return
            sql="select *from review where book_id=%s"
            values=(book,)
            mycursor.execute(sql,values)
            rows=mycursor.fetchall()
            x2=0
            y2=30
            a=Label(root2,text="The review of this book is:").pack()
            for i in rows:
                a = Label(root2, font=("Helvetica", 15, "bold"),text=f"{i[2]}\n--{i[1]}").place(x=x2,y=y2)
                y2+=100
            root2.mainloop()
            pass
        mycursor = None
        root = Tk()
        root.title("Return")
        root.geometry('800x800')
        root.config(bg="#1F2739")  # Set background color

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2003",
                database="project"
            )
            mycursor = mydb.cursor()
        except mysql.connector.Error as err:
            print(f"{err}")
            messagebox.showerror("Error", "Failed to connect to the database.")
            root.destroy()
            return
        frame1 = Frame(root, bg="#1F2739", width=400, height=800)
        frame2 = Frame(root, bg="#1F2739", width=400, height=800)
        frame1.grid(row=1, column=0)
        frame2.grid(row=1, column=1)
        a=Label(root,text="Review",font=("Helvetica", 36, "bold"), bg="#1F2739", fg="#F2C14E").grid(row=0,column=1)
        sql="select currently_borrowing from users where email=%s"
        values=(user,)
        mycursor.execute(sql,values)
        rows1=mycursor.fetchall()
        rows3=json.loads(rows1[0][0])
        sql = "select link,book_name,book_id from borrow"
        mycursor.execute(sql)
        rows2= mycursor.fetchall()
        x1=0
        y1=0
        for i in rows3:
            for j in rows2:
                if i==j[1]:
                    img = ImageTk.PhotoImage(Image.open(j[0]))
                    button = Button(frame1, image=img,command=lambda book=j[2]:display(book))
                    button.image = img
                    button.grid(row=y1, column=0, padx=20, pady=20)
                    self.text_entry = Text(frame2, font=("Helvetica", 14), height=10, width=30)
                    self.text_entry.grid(row=y1, column=0, padx=20, pady=20)
                    button1=Button(frame2,text="Submit",command=lambda book=j[2]:enter(book))
                    button1.grid(row=y1,column=1)
                    y1+=200
                    pass