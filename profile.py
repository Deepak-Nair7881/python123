from tkinter import *
import json
from PIL import ImageTk, Image
import datetime
from datetime import date
from tkinter import messagebox
import mysql.connector

import borrow


class profile1:
    def __init__(self):
        self.root=None
        self.c=0
        pass
    def profile2(self,user):
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
        sql="select email,dob,currently_borrowing,fine from users where email=%s"
        values=(user,)
        mycursor.execute(sql,values)
        rows=mycursor.fetchall()
        name=['Name:','D0B:','Currently Borrowed:','Fine:']
        rows1=rows[0]
        # print(rows1)
        frame = Frame(root, width=400, height=400)
        frame.pack(pady=200)

        i = 0
        for value in rows1:
            name_label = Label(frame, text=f"{name[i]} {value}", font=("Helvetica", 12, "bold"))
            name_label.pack(anchor=W,pady=(0,10))
            i+=1
        if rows1[3]!=0:
            button_label=Button(frame,text="Pay fine",font=("Helvetica", 12, "bold"))
            button_label.pack(anchor=W,pady=(0,10))
        # profile_text = Label(root, font=("Helvetica", 12), wrap=WORD)
        # profile_text.pack(padx=10, pady=10)
        #
        # # Insert the profile data into the text widget
        # i=0
        # for value in rows1:
        #     profile_text.insert(END, name[i] + "\n", 'label')
        #     profile_text.insert(END, str(value) + "\n\n", 'value')
        #     i+=1
        #
        # # Configure tags for label and value styles
        # profile_text.tag_configure('label', font=("Helvetica", 12, "bold"))
        # profile_text.tag_configure('value', font=("Helvetica", 12))
        # profile_text.tag_configure('button', foreground="blue", underline=True)
        # profile_text.tag_bind('button', '<Button-1>',borrow.borrow1)

        root.mainloop()