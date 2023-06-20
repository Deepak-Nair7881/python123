from tkinter import *
import json
from PIL import ImageTk, Image
import datetime
from datetime import date
from tkinter import messagebox
import mysql.connector

class return2:
    def __init__(self):
        self.root=None
        self.img = None
        self.total = 0
        self.c = 0

    def return3(self, user):

        mycursor = None
        root = Tk()
        root.title("Return")
        root.geometry('800x800')
        root.config(bg="#1F2739")  # Set background color

        def refresh_window():
            # Clear existing widgets
            for widget in root.winfo_children():
                widget.destroy()
            # Reload the updated book list
            self.return3(user)

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

        a = Label(root, text="Return", font=("Helvetica", 36, "bold"), bg="#1F2739", fg="#F2C14E")  # Set label font and colors
        a.pack(pady=20)

        sql = "SELECT currently_borrowing FROM users WHERE email=%s;"
        values = (user,)
        mycursor.execute(sql, values)
        rows = mycursor.fetchall()
        cur = json.loads(rows[0][0])

        if len(cur) == 0:
            messagebox.showinfo("Alert", "Nothing borrowed yet")
            root.destroy()
            return

        sql = "SELECT link, book_name, date_of_returning, currently_borrowed FROM borrow"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        x1 = 0
        y1 = 0

        for i in rows:
            def return_book(book, fine):
                if fine == 0:
                    sql = "UPDATE borrow SET currently_borrowed=%s WHERE book_name=%s"
                    values = (False, book)
                    mycursor.execute(sql, values)

                    sql = "UPDATE borrow SET date_of_borrowing=%s WHERE book_name=%s"
                    values = (None, book)
                    mycursor.execute(sql, values)

                    sql = "UPDATE borrow SET date_of_returning=%s WHERE book_name=%s"
                    values = (None, book)
                    mycursor.execute(sql, values)

                    sql = "SELECT currently_borrowing FROM users WHERE email=%s;"
                    values = (user,)
                    mycursor.execute(sql, values)
                    rows = mycursor.fetchall()
                    cur = json.loads(rows[0][0])
                    cur = [i for i in cur if i != book]
                    cur2 = json.dumps(cur)

                    sql = "UPDATE users SET currently_borrowing=%s WHERE email=%s"
                    values = (cur2, user)
                    mycursor.execute(sql, values)

                    sql = "UPDATE users SET fine=fine+%s WHERE email=%s"
                    values = (fine, user)
                    mycursor.execute(sql, values)
                    messagebox.showinfo("Success", "Book returned successfully")

                    sql = "SELECT previously_used_by FROM borrow WHERE book_name=%s;"
                    values = (book,)
                    mycursor.execute(sql, values)
                    rows = mycursor.fetchall()
                    cur = json.loads(rows[0][0])
                    if user not in cur:
                        cur.append(user)
                        cur2 = json.dumps(cur)
                        sql = "UPDATE borrow SET previously_used_by=%s WHERE book_name=%s"
                        values = (cur2, book)
                        mycursor.execute(sql, values)

                    sql = "SELECT number_of_times FROM borrow WHERE book_name=%s;"
                    values = (book,)
                    mycursor.execute(sql, values)
                    rows=mycursor.fetchall()
                    c=rows[0][0]
                    c+=1
                    sql = "UPDATE borrow SET number_of_times=%s WHERE book_name=%s"
                    values = (c, book)
                    mycursor.execute(sql, values)
                    # rows[0][0]=rows[0][0]+1

                    mydb.commit()
                    messagebox.showinfo("Success", "Book returned successfully")
                    root.destroy()
                    self.return3(user)


                else:
                    self.total += fine
                    sql = "UPDATE borrow SET currently_borrowed=%s WHERE book_name=%s"
                    values = (False, book)
                    mycursor.execute(sql, values)

                    sql = "UPDATE borrow SET date_of_borrowing=%s WHERE book_name=%s"
                    values = (None, book)
                    mycursor.execute(sql, values)

                    sql = "UPDATE borrow SET date_of_returning=%s WHERE book_name=%s"
                    values = (None, book)
                    mycursor.execute(sql, values)

                    sql = "SELECT currently_borrowing FROM users WHERE email=%s;"
                    values = (user,)
                    mycursor.execute(sql, values)
                    rows = mycursor.fetchall()
                    cur = json.loads(rows[0][0])
                    cur = [i for i in cur if i != book]
                    cur2 = json.dumps(cur)

                    sql = "UPDATE users SET currently_borrowing=%s WHERE email=%s"
                    values = (cur2, user)
                    mycursor.execute(sql, values)

                    sql = "UPDATE users SET fine=fine+%s WHERE email=%s"
                    values = (fine, user)
                    mycursor.execute(sql, values)

                    mydb.commit()
                    messagebox.showinfo("Success", "Book returned successfully with a fine")


            if i[1] in cur:
                if i[2] > date.today() and i[3]:
                    self.img = ImageTk.PhotoImage(Image.open(i[0]))
                    button = Button(root, image=self.img, command=lambda book=i[1], fine=0: return_book(book, fine),
                                    bg="#1F2739", relief=FLAT)  # Set button color and style
                    button.image = self.img
                    button.place(x=100 + x1, y=100 + y1)

                    a = Label(root, text=i[1], font=("Helvetica", 14), bg="#1F2739", fg="#F2C14E")  # Set label font and colors
                    a.place(x=100 + x1, y=200 + y1)

                    x1 += 100
                else:
                    self.img = ImageTk.PhotoImage(Image.open(i[0]))
                    date_diff = (date.today() - i[2]).days
                    fine = date_diff * 10
                    button = Button(root, image=self.img, command=lambda book=i[1], fine=fine: return_book(book, fine),
                                    bg="#1F2739", relief=FLAT)  # Set button color and style
                    button.image = self.img
                    button.place(x=100 + x1, y=100 + y1)

                    a = Label(root, text=i[1], font=("Helvetica", 14, "bold"), fg='#FF5A5F', bg="#1F2739")  # Set label font and colors
                    a.place(x=100 + x1, y=200 + y1)

                    x1 += 100

        root.mainloop()



