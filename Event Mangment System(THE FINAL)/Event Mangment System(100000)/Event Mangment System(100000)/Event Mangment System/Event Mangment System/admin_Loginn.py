import customtkinter as ctk
from tkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
import os
import sqlite3
from tkinter import messagebox


def back():
    root1.destroy()
    os.system("python login_as.py")


def login_admin():
    conn = sqlite3.connect("database.db")
    adminconnect = conn.cursor()
    adminconnect.execute("SELECT * from admin WHERE user_name= ? and password= ?",
                         (Enter_user.get(), Enter_password.get()))
    user = adminconnect.fetchone()
    conn.close()

    if not user:
        messagebox.showerror(title="Login",
                      message="Username or password incorrect!",
                      # button_color="#7B9976",
                      # button_hover_color="#7B9976",
                      # bg_color="#262724",
                      # font=('Times New Roman', 15, 'bold'),
                      # icon="warning",
                      # fg_color="#7B9976",
                      # title_color="#7B9976",
                      # option_1="OK",
                      # button_text_color="#262724")
                             )
    else:
        messagebox.showinfo(title='Login',
                      message="Successfully logged in",
                      # button_color="#7B9976",
                      # button_hover_color="#7B9976",
                      # bg_color="#262724",
                      # font=('Times New Roman', 20),
                      # icon=None,
                      # fg_color="#7B9976",
                      # title_color="#7B9976",
                      # option_1="OK",
                      # button_text_color="#262724",
                      # button_height=15,
                      # width=550,
                      # height=150, )
        )
        root1.destroy()
        os.system("python adminpage.py")


def hide():
    hide_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show, hover_color='#7E9779',
                             text='', width=5, height=5)
    hide_but.place(x=500, y=255)
    Enter_password.configure(show='*')


def show():
    show_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=show_image, command=hide, hover_color='#7E9779',
                             text='', width=5, height=5)
    show_but.place(x=500, y=255)
    Enter_password.configure(show='')


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


root1 = ctk.CTk()
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
center_x = 0
center_y = 0
root1.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
root1.title("Event Management System")
root1.iconbitmap("assests/ticket_856232.ico")
img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root1, image=img1)
label_photo.pack()

loginFrame = ctk.CTkFrame(root1, corner_radius=40, width=700, height=500, bg_color="#7b987e")
loginFrame.place(x=70, y=200)

title = ctk.CTkLabel(loginFrame, text='Login', pady=15, font=('Times New Roman', 50, 'bold'), text_color="#7B9976")
title.place(relx=0.5, y=90, anchor=ctk.CENTER)

# slogan = ctk.CTkLabel(loginFrame, text='Its time to have fuuuuuuun', pady=15, font=('Times New Roman', 20),
#                       text_color="#7B9976")
# slogan.place(relx=0.5, y=120, anchor=ctk.CENTER)

Enter_user = ctk.CTkEntry(loginFrame, placeholder_text='Username', corner_radius=10, width=280, height=30)
Enter_user.place(relx=0.5, y=220, anchor=ctk.CENTER)

Enter_password = ctk.CTkEntry(loginFrame, placeholder_text='Password', show='*', corner_radius=10, width=280,
                              height=30)
Enter_password.place(relx=0.5, y=275, anchor=ctk.CENTER)

but_Login = ctk.CTkButton(loginFrame, text='Login', font=('Times New Roman', 20, 'bold'), fg_color="#7B9976",
                          hover_color="#9CBB9F", text_color='#262724', command=login_admin)
but_Login.place(relx=0.5, y=360, anchor=ctk.CENTER)

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(loginFrame, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9976',
                         command=back)
but_back.place(x=20, y=20)

hide_image = ImageTk.PhotoImage(file='assests/eye.png')
show_image = ImageTk.PhotoImage(file='assests/view.png')
show_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show, hover_color='#7E9779', text='',
                         width=5, height=5, corner_radius=5)
show_but.place(x=500, y=255)

change_theme_box = ctk.CTkSwitch(master=root1, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root1.mainloop()
