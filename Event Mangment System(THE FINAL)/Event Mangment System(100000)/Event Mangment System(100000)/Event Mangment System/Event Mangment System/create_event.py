import os
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from tkcalendar import DateEntry

def delete():
    entryname.delete(0, 'end')
    entryid.delete(0, 'end')
    entryTime.delete(0, 'end')
    entryduration.delete(0, 'end')

def is_all_digits(s):
    return s.isdigit()

def back():
    root.destroy()
    os.system("python adminpage.py")


def submit():
    event_name = entryname.get()
    event_id = entryid.get()
    event_date = entrydate.get_date()
    event_time = entryTime.get()
    event_duration = entryduration.get()

    # Check if any field is empty
    if not event_name or not event_id or not event_date or not event_time or not event_duration:
        messagebox.showwarning("Missing Fields", "Please fill out all fields.")
        return
    if is_all_digits(event_id) and is_all_digits(event_time) and is_all_digits(event_duration):
        conn = sqlite3.connect("database.db")
        createconncetion = conn.cursor()
        createconncetion.execute(
            "INSERT INTO event(event_name, event_id, event_date, event_time, event_duration) VALUES(?,?,?,?,?)",
            (event_name, event_id, event_date, event_time, event_duration))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success!!", "Event created successfully!!")
        root.destroy()
        os.system("python adminpage.py")
    else:
        messagebox.showwarning("Error","(Event_id , Event_time , Event_duration) must contain numbers only!!")

def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


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

loginFrame = ctk.CTkFrame(root, corner_radius=60, width=700, height=600,bg_color="#7b987e")
loginFrame.place(x=90, y=60)

datelis_image = ImageTk.PhotoImage(file='assests/form (1).png')
imagelabel = ctk.CTkLabel(loginFrame, image=datelis_image, text='')
imagelabel.place(x=450, y=20)

labelText = ctk.CTkLabel(loginFrame, text='Enter details.', text_color='#7B9B75', pady=10,
                         font=('Times New Roman', 50, 'bold'))
labelText.place(x=150, y=10)

labelname = ctk.CTkLabel(loginFrame, text='Event Name', text_color='#7B9B75', pady=10,
                         font=('Times New Roman', 30, 'bold'))
labelname.place(x=40, y=120)

labelid = ctk.CTkLabel(loginFrame, text='Event ID', text_color='#7B9B75', pady=10, font=('Times New Roman', 30, 'bold'))
labelid.place(x=40, y=190)

labeldate = ctk.CTkLabel(loginFrame, text='Event Date', text_color='#7B9B75', pady=10,
                         font=('Times New Roman', 30, 'bold'))
labeldate.place(x=40, y=260)

labelTime = ctk.CTkLabel(loginFrame, text='Event Time', text_color='#7B9B75', pady=10,
                         font=('Times New Roman', 30, 'bold'))
labelTime.place(x=40, y=330)

labelduration = ctk.CTkLabel(loginFrame, text='Event Duration', text_color='#7B9B75', pady=10,
                             font=('Times New Roman', 30, 'bold'))
labelduration.place(x=40, y=400)

# Entry ....
entryname = ctk.CTkEntry(loginFrame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                         placeholder_text='Enter Name as Football match')
entryname.place(x=350, y=135)

entryid = ctk.CTkEntry(loginFrame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                       placeholder_text='Enter ID as 44611697')
entryid.place(x=350, y=200)

entrydate = DateEntry(loginFrame, width=27, background='#7B9B75', font=('Times New Roman', 20, 'bold'))
entrydate.place(x=420, y=330)

entryTime = ctk.CTkEntry(loginFrame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                         placeholder_text='Enter Time as 10 PM')
entryTime.place(x=350, y=345)

entryduration = ctk.CTkEntry(loginFrame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                             placeholder_text='Enter Duration as 8/8/2024')
entryduration.place(x=350, y=415)

done_image = ImageTk.PhotoImage(file='assests/subb.png')
but_submit = ctk.CTkButton(loginFrame, text='Submit', text_color='#262724', fg_color='#7B9976', hover_color="#9CBB9F",
                           font=('Times New Roman', 30, 'bold'), image=done_image, command=submit)
but_submit.place(x=430, y=490)

delete_image = ImageTk.PhotoImage(file='assests/recycle-bin (1).png')
but_delete = ctk.CTkButton(loginFrame, text='Delete', text_color='#262724', fg_color='#7B9976',hover_color="#9CBB9F",
                           font=('Times New Roman', 30, 'bold'), image=delete_image, command=delete)
but_delete.place(x=100, y=490)

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(loginFrame, text='', fg_color='#262724', hover_color='#7B9976', image=back_image, width=40,
                         command=back)
but_back.place(x=20, y=20)

change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724', fg_color='#262724',
                                 font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)

root.mainloop()
