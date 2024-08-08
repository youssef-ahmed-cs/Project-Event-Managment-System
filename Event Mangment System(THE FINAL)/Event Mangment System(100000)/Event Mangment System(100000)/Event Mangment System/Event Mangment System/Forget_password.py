import sqlite3
from tkinter import messagebox
from tkinter import *
import os
import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk


def back():
    root.destroy()
    os.system("python User_Loginn.py")


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")




def check_security_question():
    conn=sqlite3.connect("database.db")
    forget=conn.cursor()
    forget.execute("SELECT* from user WHERE username=? and mother_name=?", (Enter_username.get(),Enter_mother_name.get()))
    user=forget.fetchone()
    if user:
        conn.close()
        root.destroy()
        os.system("python forgetpasswordchange.py")
    else:
        messagebox.showerror(title="Error",message="Invaild username or Incorrect Mother name"
                      )



root = ctk.CTk()

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

root.title('Event management system')
root.iconbitmap('assests/ticket_856232.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')

img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root, image=img1)
label_photo.pack()
forgotPasswordFrame = ctk.CTkFrame(root, corner_radius=60, width=700, height=500,bg_color="#7b987e")
forgotPasswordFrame.place(x=70, y=200)
title = ctk.CTkLabel(forgotPasswordFrame, text='Forgot Password', pady=15, font=('Times New Roman', 30, 'bold'),
                     text_color="#7B9976")
title.place(relx=0.5, y=50, anchor=tk.CENTER)

Enter_username = ctk.CTkEntry(forgotPasswordFrame, placeholder_text='Username', corner_radius=10, width=280, height=30)
Enter_username.place(relx=0.5, y=150, anchor=tk.CENTER)

Enter_mother_name = ctk.CTkEntry(forgotPasswordFrame, placeholder_text="What's your mother's name?", corner_radius=10,
                                 width=280, height=30)
Enter_mother_name.place(relx=0.5, y=200, anchor=tk.CENTER)
but_Submit = ctk.CTkButton(forgotPasswordFrame, text='Submit', font=('Times New Roman', 20, 'bold'),
                           hover_color='#9CBB9F', text_color='#262624', bg_color='#262624', fg_color='#7B9976',
                           command=check_security_question)
back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(forgotPasswordFrame, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9976',
                         command=back)
but_back.place(x=30, y=20)
but_Submit.place(relx=0.5, y=250, anchor=tk.CENTER)

change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)

root.mainloop()
