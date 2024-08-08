import os
import tkinter
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


def settingsbutton():
    root.destroy()
    os.system("python settings._admin.py")


def createbutton():
    root.destroy()
    os.system("python create_event.py")


def cancelevent():
    root.destroy()
    os.system("python cancel_event.py")


def exitt():
    root.destroy()
    os.system("python login_as.py")


root = ctk.CTk()
ctk.set_appearance_mode('system')
root.title('Event management system')
root.iconbitmap('assests/ticket_856232.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root, image=img1)
label_photo.image = img1
label_photo.pack()

inner_frame = ctk.CTkFrame(root, corner_radius=60, width=600, height=500,bg_color="#7b987e")
inner_frame.place(relx=0.3, rely=0.47, anchor=tkinter.CENTER)

labelText = ctk.CTkLabel(inner_frame, text='Admin', pady=10, text_color='#7B9B75', font=('Times New Roman', 50, 'bold'))
labelText.place(x=230, y=15)
exiticon = ImageTk.PhotoImage(file='assests/exitt.png')
but_exit = ctk.CTkButton(inner_frame, corner_radius=20, text='Log out', text_color='#262724', fg_color='#7B9976',
                        hover_color="#9CBB9F", font=('Times New Roman', 30, 'bold'), image=exiticon,
                         command=exitt)
but_exit.place(x=250, y=330)
cancelicon = PhotoImage(file='assests/cancel.png')
but_Cancel_Event = ctk.CTkButton(inner_frame, corner_radius=20, text_color='#262724', fg_color='#7B9976',
                                 hover_color="#9CBB9F", text='Edit Events', font=('Times New Roman', 30, 'bold'),
                                 image=cancelicon, command=cancelevent)
but_Cancel_Event.place(x=330, y=230)
iconcreate = ImageTk.PhotoImage(file='assests/plusss.png')
but_create = ctk.CTkButton(inner_frame, corner_radius=20, text_color='#262724', fg_color='#7B9976',
                           hover_color="#9CBB9F", text='Create Event', font=('Times New Roman', 30, 'bold'), width=70,
                           image=iconcreate, command=createbutton)
but_create.place(x=70, y=230)
back_image = ImageTk.PhotoImage(file='assests/gear.png')
but_back = ctk.CTkButton(inner_frame, text='', fg_color='#262724', image=back_image, width=40,
                         hover_color='#7B9976', command=settingsbutton)

but_back.place(x=530, y=20)

change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724', fg_color='#262724',
                                 font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root.mainloop()
