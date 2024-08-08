import os

import customtkinter as ctk
import tkinter
from tkinter import *
from PIL import Image, ImageTk


def bookking():
    root.destroy()
    os.system("python Book.py")


def viewbutton():
    root.destroy()
    os.system("python viewticketsuser.py")


def cancelbutton():
    root.destroy()
    os.system("python cancelticket.py")


def logout():
    root.destroy()
    os.system("python login_as.py")


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


def settings():
    root.destroy()
    os.system("python Settings_user.py")


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
labelText = ctk.CTkLabel(inner_frame, font=('Times New Roman', 50, 'bold'), text='User', pady=10, text_color='#7E9779')
labelText.place(x=240, y=15)
exiticon = ImageTk.PhotoImage(file='assests/exitt.png')
but_exit = ctk.CTkButton(inner_frame, corner_radius=20, text='Log out', text_color='#262724', fg_color='#7B9976',
                         hover_color="#9CBB9F", command=logout,
                         font=('Times New Roman', 30, 'bold'), image=exiticon, )
but_exit.place(x=230, y=400)
viewTicketimage = PhotoImage(file='assests/wiewww.png')
bookingImage = PhotoImage(file='assests/booking.png')
cancelTicketImage = PhotoImage(file='assests/cancel.png')
bookinButton = ctk.CTkButton(inner_frame, corner_radius=20, image=bookingImage, text='Booking ticket',
                             text_color='#262724',hover_color="#9CBB9F", fg_color='#7E9779',
                             font=('Times New Roman', 30, 'bold'), command=bookking, width=40, ).place(x=185, y=155)
cancelButton = ctk.CTkButton(inner_frame, corner_radius=20, image=cancelTicketImage, text='cancel ticket',
                             fg_color='#7E9779',hover_color="#9CBB9F",command=cancelbutton, text_color='#262724',
                             font=('Times New Roman', 30, 'bold',), width=45).place(x=200, y=322)
viewButton = ctk.CTkButton(inner_frame, corner_radius=20, image=viewTicketimage, text='view Event',
                           fg_color='#7E9779',hover_color="#9CBB9F", text_color='#262724',
                           font=('Times New Roman', 30, 'bold'), command=viewbutton,width=45).place(x=200, y=235)
back_image = ImageTk.PhotoImage(file='assests/gear.png')
but_back = ctk.CTkButton(inner_frame, text='', fg_color='#262724', image=back_image, width=40,
                         command=settings,
                         hover_color='#7B9B75')

but_back.place(x=530, y=20)
change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root.mainloop()
