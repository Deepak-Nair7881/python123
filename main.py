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
def main_page(user,root):
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
def signuo(root):
  def insert():
    username=user_name2.get()
    password=user_name1.get()
    date=datetime.datetime.strptime(cal.get(), '%m/%d/%y').strftime('%Y-%m-%d')
    mobile=mob.get()
    sql = "INSERT INTO users (email,passw ,DOB ,PH_NO ,currently_borrowing) VALUES (%s, %s, %s, %s,'[]')"
    val = (username, password, date, mobile)
    mycursor.execute(sql, val)
    mydb.commit()

    # print a success message
    print(mycursor.rowcount, "record inserted.")
    mydb.close()
    main_page(username,root1)
  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="2003",
      database="project"
    )
    mycursor=mydb.cursor()
  except mysql.connector.Error as err:
    print(f"{err}")
  finally:
    print("success")

  root.destroy()
  root1 = Tk()
  root1.title("Library System 1.1.0")
  root1.geometry('925x500+300+200')
  root1.resizable(False, False)
  frame=Frame(root1,width=350,height=450,bg="white")
  frame.place(x=480,y=70)
  # img = ImageTk.PhotoImage(Image.open('WhatsApp Image 2023-05-12 at 15.38.54.jpg'))
  # Label(root1, image=img, bg='white').place(x=50, y=50)
  frame = Frame(root1, width=350, height=450, bg='white', border=0)
  frame.place(x=480, y=70)
  heading = Label(frame, text='Sign Up ', fg='#57a1f8', bg='white', font=('Microsoft YaHHei UI Light', 18, 'bold'))
  heading.place(x=45, y=5)
  # label = Label(frame, text="Username:", bg='White', fg='black', font=('Microsoft YaHHei UI Light', 9))
  # label.place(x=70, y=80)
  # user_name1 = Entry(frame,width=25,border=0,font=("times new roman", 10, "bold"), bg="white", fg="black")
  # user_name1.place(x=70, y=100)
  # user_name1.insert(0,'Desired  Pass: ')
  # label = Label(frame, text="Password: ", bg='white', fg='black', font=('Microsoft YaHHei UI Light', 9))
  # label.place(x=70, y=140)
  ####
  user_name2 = Entry(frame, width=25, border=0, font=("times new roman", 11), bg="white", fg="black")
  user_name2.place(x=30, y=80)
  user_name2.insert(0, 'Desired Username: ')
  Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
  user_name1 = Entry(frame,width=25,border=0,font=("times new roman", 10), bg="white", fg="black",show="*")
  user_name1.place(x=30, y=150)
  user_name1.insert(0,'Desired  Pass: ')
  Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
  cal = DateEntry(frame, width=25, border=0, font=("times new roman", 10), bg="white", fg="black")
  cal.place(x=30, y=220)
  Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
  mob= Entry(frame, width=25, border=0, font=("times new roman", 10), bg="white", fg="black")
  mob.place(x=30, y=290)
  mob.insert(0, 'Desired  mobile: ')
  Frame(frame, width=295, height=2, bg='black').place(x=25, y=310)
  Button(frame, width=20, pady=7, text="Register", bg='#57a1f8', fg='white', border=2, padx=10, command=insert).place(x=35,y=360)
  label=Label(frame,text="To Go Back click here: ",fg='black',bg='white',font=("times new roman",9))
  label.place(x=75,y=450)
  back=Button(frame,width=6,text="Back",bg='white',cursor='hand2',fg="#57a1f8",command=main_page)
  back.place(x=215,y=500)
  root1.mainloop()
def login(root):
  def check():
    email=user_name2.get()
    password=user_name1.get()
    query = "SELECT * FROM users where email=%s"
    values=(email,)
    try:
      mycursor.execute(query,values)
    except mysql.connector.errors as err:
      messagebox.showinfo(title="Alert", message="Login Unsuccessful")
      print(f"Error is:{err}")
    finally:
      messagebox.showinfo(title="Alert",message="Login Successful")
      main_page(email,root1)
    # rows=mycursor.fetchall()
    # print(rows)
    # for i in rows:
    #   if i[0]==email and i[1]==password:
    #     messagebox.showinfo(title="Alert",message="login success")
    #     a = Label(root1, text="Login successful").place(x=100,y=220)
    #     main_page(email)
    #   else:
    #     messagebox.showinfo(title="Alert", message="login failed")
    #     a = Label(root1, text="Login failed").place(x=100, y=220)
    #     break

  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="2003",
      database="project"
    )
    mycursor=mydb.cursor()
  except mysql.connector.Error as err:
    print(f"{err}")
  finally:
    print("success")
  root.destroy()
  root1 = Tk()
  root1.title("Library System 1.1.0")
  root1.geometry('925x500+300+200')
  root1.resizable(False, False)
  frame = Frame(root1, width=350, height=350, bg="white")
  frame.place(x=480, y=70)
  # img = PhotoImage(file='login.png')
  # Label(root1, image=img, bg='white').place(x=50, y=50)
  frame = Frame(root1, width=350, height=350, bg='white', border=0)
  frame.place(x=480, y=70)
  heading = Label(frame, text='Sign Up ', fg='#57a1f8', bg='white', font=('Microsoft YaHHei UI Light', 18, 'bold'))
  heading.place(x=45, y=5)
  # label = Label(frame, text="Username:", bg='White', fg='black', font=('Microsoft YaHHei UI Light', 9))
  # label.place(x=70, y=80)
  # user_name1 = Entry(frame,width=25,border=0,font=("times new roman", 10, "bold"), bg="white", fg="black")
  # user_name1.place(x=70, y=100)
  # user_name1.insert(0,'Desired  Pass: ')
  # label = Label(frame, text="Password: ", bg='white', fg='black', font=('Microsoft YaHHei UI Light', 9))
  # label.place(x=70, y=140)
  ####
  user_name2 = Entry(frame, width=25, border=0, font=("times new roman", 11), bg="white", fg="black")
  user_name2.place(x=30, y=80)
  user_name2.insert(0, 'Enter Username: ')
  Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
  user_name1 = Entry(frame, width=25, border=0, font=("times new roman", 10), bg="white", fg="black", show="*")
  user_name1.place(x=30, y=150)
  user_name1.insert(0, 'Enter Pass: ')
  Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
  Button(frame, width=20, pady=7, text="Sign In: ", bg='#57a1f8', fg='white', border=2, padx=10, command=check).place(
    x=35, y=230)
  label = Label(frame, text="To Go Back click here: ", fg='black', bg='white', font=("times new roman", 9))
  label.place(x=75, y=270)
  back = Button(frame, width=6, text="Back", bg='white', cursor='hand2', fg="#57a1f8", command=main_page)
  back.place(x=215, y=270)
  root1.mainloop()
root1 = Tk()
root1.title("Library System 1.1.0")
root1.geometry('925x500+300+200')
root1.resizable(False,False)
img=ImageTk.PhotoImage(Image.open('WhatsApp Image 2023-05-12 at 15.38.54.jpg'))
Label(root1,image=img,bg='white').place(x=50,y=50)
frame=Frame(root1,width=350,height=350,bg='white',border=0)
frame.place(x=480,y=70)
heading=Label(frame,text='Welcome to Library\nSystem 1.10',fg='#57a1f8',bg='white',font=('Microsoft YaHHei UI Light',18,'bold'))
heading.place(x=45,y=5)
label=Label(frame,text="Have  One? ",bg='White',fg='black',font=('Microsoft YaHHei UI Light',9))
label.place(x=50,y=80)
label=Label(frame,text="Don't Have One? ",bg='white',fg='black',font=('Microsoft YaHHei UI Light',9))
label.place(x=70,y=180)
Button(frame,width=20,pady=10,text="Use me as REGISTER Button;",bg='#57a1f8',fg='white',border=2,padx=10,command=lambda root=root1: signuo(root)).place(x=60,y=200)
Button(frame,width=20,pady=10,text="Use Me as LOGIN Button",bg='#57a1f8',fg='white',border=2,command=lambda root=root1: login(root)).place(x=130,y=100)
root1.mainloop()
# main_page('hello12345')


