from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import threading
import random
from twilio.rest import Client
import os
import sys
#---------------------------------------------
global z
z=0
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#-------------------------------------------------------
def update_timer():
    global remaining_time
    timer_label = tk.Label(root,bg="white",fg="green", text=f"Otp will be sent in {remaining_time} seconds          ", font=("cambria", 11))
    timer_label.place(x=558,y=400)
    
    remaining_time -= 1
    if remaining_time >= 0:
        timer_label.config(text=f"Otp will be sent in {remaining_time} seconds          ")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="OTP has been successfully sent. ")
        remaining_time=10
        root.after(1000)
        field()
#---------------------------------------------------------------------
def field():
    otp=0
    def check():
        global otp
        if otp_field.get()=="":
            messagebox.showinfo("Alert","Please Enter the Code")
        elif int(otp_field.get()):
            b = int(otp_field.get())
            if b == otp:
                messagebox.showinfo("Alert","The OTP verification is successful.")
                otp_field.place(x=-1000, y=-1000)
                f.place(x=-1000, y=-1000)
                a.place(x=-1000, y=-1000)
                timer_label = tk.Label(root,bg="white",fg="green", text="                                                                      ", font=("cambria", 11))
                timer_label.place(x=558,y=400)
                user.delete(0,"end")
                code.delete(0,"end")
                code.config(show="*",font=("Microsoft YaHei UI Light",15))
                user.insert(0,"33050409003")
                code.insert(0,"svv2014#")
            else:
                messagebox.showerror("Alert","Incorrect Otp ,Please try again !.")
    
    def sendotp():
        global otp
        otp = random.randint(1000, 9999)
        sid = " " # sending id
        auth = " " # receiving id
        cli = Client(sid, auth)
        mg = cli.messages.create(
            body=f"your OTP is {otp}",
            from_="+12092458297",
            to=" " ## to number
        )

    try:
        sendotp()
    except Exception:
        global time_label
        time_label=Label(root,bg="white",text=" Please Check Your Internet !    ",fg="red",font=("cambria", 11))
        time_label.place(x=558,y=400)
        timer_label.place(x=-1000,y=-1000)
        global z
        z=1
    if z==0:
        def validate_numeric_input(event):
            char = event.char
            if not char.isdigit() and char != '\b':
                return 'break'
            else:
                return None
        def on_enter(e):
            otp_field.delete(0,'end')
            otp_field.config(show="*",font=("Microsoft YaHei UI Light",15))
        def on_leave(e):
            name=otp_field.get()
            if name=='':
                otp_field.insert(0,' Enter Code')
                otp_field.config(show="",font=("Microsoft YaHei UI Light",11))
        otp_field=tk.Entry(root,width=10,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11),validatecommand=(validate_numeric_input, '%S'))
        otp_field.place(x=563,y=430)
        otp_field.insert(0,' Enter Code')
        otp_field.bind('<Key>', validate_numeric_input)
        otp_field.bind('<FocusIn>',on_enter)
        otp_field.bind('<FocusOut>',on_leave)
        a=tk.Button(root,width=11,pady=2,text='Submit',bg='#316cf4',fg='white',border=0,font=("cambria",10,'bold'),command=check)
        a.place(x=670,y=430)
        f=tk.Frame(root,width=100,height=2,bg='black')
        f.place(x=558,y=458)
def timer():
    update_timer()
    if z==1:
        time_label.place(x=-1000,y=-1000)
#------------------------------------------------------
def login():
    username = user.get()
    password = code.get()
    if username == "33050409003" and password == "svv2014#":
        messagebox.showinfo("Login Successful", "Successfully logged in !.")
        user.delete(0,"end")
        code.delete(0,"end")
        user.insert(0,"Username")
        code.insert(0,"Password")
        code.config(show="",font=("Microsoft YaHei UI Light",11))
        try:
            sid = " " # sending id
            auth = " " # receiving id
            cli = Client(sid, auth)
            mg = cli.messages.create(
                body="Dear ,Greetings! You have successfully signed in to the fees management system!",
                from_="+12092458297",
                to=" " ## to number
            )
        except Exception :
            pass
            
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    user.delete(0,"end")
    code.delete(0,"end")
    user.insert(0,"Username")
    code.insert(0,"Password")
    code.config(show="",font=("Microsoft YaHei UI Light",11))
#----------------------------------------------------
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
img=PhotoImage(file=resource_path('login.png'))
Label(root,image=img,bg="white").place(x=50,y=50)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text='Sign In',fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)
###--------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
###--------------------------------------------
def on_enter(e):
    code.delete(0,'end')
    code.config(show="*",font=("Microsoft YaHei UI Light",15))
    show_hide_button.config(image=eye_open_image)
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        code.config(show="",font=("Microsoft YaHei UI Light",11))
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#--------------------------------------------------------
def toggle_password_visibility():
    global show_password
    a=code.get()
    if a=='Password':
        pass
    elif show_password:
        code.config(show="",font=("Microsoft YaHei UI Light",11))
        show_hide_button.config(image=eye_closed_image)
    else:
        code.config(show="*",font=("Microsoft YaHei UI Light",15))
        show_hide_button.config(image=eye_open_image)
    show_password = not show_password
eye_open = Image.open(resource_path("eye_open.png"))
eye_closed = Image.open(resource_path("eye_closed.png"))
eye_open = Image.open(resource_path("eye_open.png")).resize((20, 20), Image.LANCZOS)
eye_closed = Image.open(resource_path("eye_closed.png")).resize((20, 20), Image.LANCZOS)
eye_open_image = ImageTk.PhotoImage(eye_open)
eye_closed_image = ImageTk.PhotoImage(eye_closed)

show_password = False
show_hide_button = Button(frame, image=eye_closed_image, command=toggle_password_visibility, bd=0,bg="white")
show_hide_button.place(x=300,y=150)
##-------------------------------------------------------
Button(frame,width=27,pady=2,text='Sign In',bg='#316cf4',fg='white',border=0,font=("cambria",13,'bold'),command=login).place(x=35,y=204)
label=Label(frame,text="--------- Other Wise ---------",fg="black",bg="white",font=("Microsoft YaHei UI Light",11))
label.place(x=75,y=265)
remaining_time = 10 
forgot=Button(frame,width=16,text='Forgot Password',border=0,bg='white',cursor='hand2',fg='#4681f4',command=timer)
forgot.place(x=115,y=300)
#--------------------------------------------------------

timer_label = tk.Label(root, text="",bg="white", font=("Helvetica", 16))
timer_label.place(x=155,y=350)
root.mainloop()
