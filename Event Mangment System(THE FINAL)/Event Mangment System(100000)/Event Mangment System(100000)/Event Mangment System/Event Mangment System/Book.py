import tkinter as tk
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sqlite3
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from tkinter import messagebox
from datetime import datetime
import random


def generate_random_id():
    return str(random.randint(10000, 99999))


x = generate_random_id()


def sunmit():
    conn = sqlite3.connect("database.db")
    submitticket = conn.cursor()
    username = name.get()
    eventname = combox.get()

    submitticket.execute("SELECT username FROM user WHERE username=?", (username,))
    useeer = submitticket.fetchone()

    if not useeer:
        messagebox.showerror(title="Error", message="Name not found", icon="warning")
        return
    else:
        submitticket.execute("INSERT INTO ticket (user_name1, event_name1) VALUES (?, ?)", (username, eventname))
        conn.commit()
        conn.close()
        messagebox.showinfo(title="Success", message="Ticket booked successfully")


def fetch_data_from_database():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM ticket')  # Change * to specific columns if needed
    data1 = cur.fetchall()
    conn.close()
    return [item[1] for item in data1]  # Assuming event name is in the second column (index 1)


def backkk():
    root1.destroy()
    os.system("python userpage.py")


def print_ticket(username, eventname):
    if not username or not eventname:
        messagebox.showerror(title="Error", message="Please enter your name and select an event, then submit.")
        return

    def update_time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")
        current_date = now.strftime("%Y-%m-%d")
        time_label.configure(text=current_time)
        date_label.configure(text=current_date)

    def Info():
        con = sqlite3.connect("database.db")
        printtiket = con.cursor()
        printtiket.execute("SELECT event_date, event_time FROM event WHERE event_name =?", (eventname,))
        event_info = printtiket.fetchone()
        event_date, event_time = event_info if event_info else ('N/A', 'N/A')

        custom_label_show.configure(text=username)
        ticket_label_show.configure(text=x)
        event_name_label_show.configure(text=eventname)
        event_date_label_show.configure(text=event_date)
        event_time_label_show.configure(text=event_time)
        event_price_label_show.configure(text='$1000.00')
        con.close()

    def cancel():
        root.destroy()

    root = ctk.CTk()
    ctk.set_appearance_mode('green')

    root.resizable(False, False)

    root.config(bg='#7d9b77')

    root.title('Ticket')
    root.geometry('500x500')
    root.title("Event Management System")
    root.iconbitmap("assests/ticket_856232.ico")
    time_label = ctk.CTkLabel(root, text="", font=("Arial", 17), bg_color='#7d9b77', text_color='#120e0e')
    time_label.place(x=400, y=20)

    date_label = ctk.CTkLabel(root, text="", font=("Arial", 17), bg_color='#7d9b77', text_color='#120e0e')
    date_label.place(x=10, y=20)

    text = ctk.CTkLabel(root, text="== Ticket ==", font=('Times New Roman', 35, 'bold'), bg_color='#7d9b77',
                        text_color='#120e0e')
    text.place(x=160, y=20)

    flabel = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabel.place(x=0, y=60)

    # ---------------------------------------------------------------

    custom_label = ctk.CTkLabel(root, text='Customer Name:', font=('Times New Roman', 20), bg_color='#7d9b77',
                                text_color='#120e0e')
    custom_label.place(x=5, y=90)

    custom_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                     text_color='#120e0e')
    custom_label_show.place(x=240, y=90)

    # ---------------------------------------------------------------

    flabe2 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe2.place(x=0, y=120)

    ticket_label = ctk.CTkLabel(root, text='Ticket ID', font=('Times New Roman', 20), bg_color='#7d9b77',
                                text_color='#120e0e')
    ticket_label.place(x=5, y=150)

    ticket_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                     text_color='#120e0e')
    ticket_label_show.place(x=240, y=150)

    # ---------------------------------------------------------------

    flabe2 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe2.place(x=0, y=180)

    event_name_label = ctk.CTkLabel(root, text='Event Name', font=('Times New Roman', 20), bg_color='#7d9b77',
                                    text_color='#120e0e')
    event_name_label.place(x=5, y=210)

    event_name_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                         text_color='#120e0e')
    event_name_label_show.place(x=240, y=210)

    # ---------------------------------------------------------------

    flabe3 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe3.place(x=0, y=240)

    event_date_label = ctk.CTkLabel(root, text='Event Date', font=('Times New Roman', 20), bg_color='#7d9b77',
                                    text_color='#120e0e')
    event_date_label.place(x=5, y=270)

    event_date_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                         text_color='#120e0e')
    event_date_label_show.place(x=240, y=270)

    # ---------------------------------------------------------------

    flabe4 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe4.place(x=0, y=300)

    event_time_label = ctk.CTkLabel(root, text='Event Time', font=('Times New Roman', 20), bg_color='#7d9b77',
                                    text_color='#120e0e')
    event_time_label.place(x=5, y=330)

    event_time_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                         text_color='#120e0e')
    event_time_label_show.place(x=240, y=330)

    # ---------------------------------------------------------------

    flabe5 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe5.place(x=0, y=360)

    event_price_label = ctk.CTkLabel(root, text='Event Price', font=('Times New Roman', 20), bg_color='#7d9b77',
                                     text_color='#120e0e')
    event_price_label.place(x=5, y=390)

    event_price_label_show = ctk.CTkLabel(root, text='', font=('Times New Roman', 20), bg_color='#7d9b77',
                                          text_color='#120e0e')
    event_price_label_show.place(x=240, y=390)

    # ---------------------------------------------------------------

    flabe6 = ctk.CTkLabel(root, text=f"{100 * '='}", bg_color='#7d9b77', text_color='#120e0e')
    flabe6.place(x=0, y=420)

    # img = ImageTk.PhotoImage(Image.open('assests\exit-full-screen.png'))
    but_cancel = ctk.CTkButton(root, text='Cancel', font=('Times New Roman', 30, 'bold'), corner_radius=15,
                               command=cancel, fg_color='#262724',
                               bg_color='#7B9976', text_color='#7B9976', hover_color='#262724')
    but_cancel.pack(side='bottom', pady=10)
    update_time()
    Info()
    root.mainloop()


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


root1 = ctk.CTk()
ctk.set_appearance_mode('system')
root1.title('Event Management System')
root1.iconbitmap('assests/ticket_856232.ico')
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
center_x = 0
center_y = 0
root1.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root1, image=img1)
label_photo.pack()

outer_frame = Frame(root1)
outer_frame.pack(padx=5, pady=0, fill=BOTH, expand=True)

inner_frame = ctk.CTkFrame(root1, corner_radius=60, width=600, height=500, bg_color="#7b987e")
inner_frame.place(relx=0.3, rely=0.47, anchor=tk.CENTER)

labelText = ctk.CTkLabel(inner_frame, text='Book Ticket', pady=10, text_color='#7B9B75',
                         font=('Times New Roman', 50, 'bold'))
labelText.place(x=180, y=15)

ctk.CTkLabel(inner_frame, text='Name', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50, y=135)
name = ctk.CTkEntry(inner_frame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                    placeholder_text='Enter Your Name as Ahmed Hassan')
name.place(x=210, y=140)

ctk.CTkLabel(inner_frame, text='Ticket Id', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50, y=215)

ticket_id = ctk.CTkEntry(inner_frame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
                         placeholder_text='Ticket Id')
ticket_id.place(x=210, y=220)
ticket_id.insert(0, f"{x}")

ctk.CTkLabel(inner_frame, text='Event', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50, y=288)
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('SELECT event_name from event')  # Change * to specific columns if needed
data1 = cur.fetchall()
conn.close()
select_value = StringVar()
combox = ttk.Combobox(inner_frame, width=20, height=30, textvariable=select_value, values=[item[0] for item in data1],
                      font=('Times New Roman', 20, 'bold'))
combox.place(x=270, y=365)
back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(root1, text='', fg_color='#7B9976', bg_color='#7B9976', image=back_image, width=40, hover_color="#262724",
                         command=backkk)
but_back.place(x=30, y=30)
submitIcon = PhotoImage(file='assests/subb.png')
ctk.CTkButton(inner_frame, text='Submit', corner_radius=20, text_color='#262724', fg_color='#7B9976',
              hover_color="#9CBB9F", font=('Times New Roman', 30, 'bold'), image=submitIcon, command=sunmit).place(
    x=100, y=400)
printbtn = ctk.CTkButton(inner_frame, text='Print ticket', corner_radius=20, text_color='#262724', fg_color='#7B9976',
                         hover_color="#9CBB9F", font=('Times New Roman', 30, 'bold'), image=submitIcon,
                         command=lambda: print_ticket(name.get(), combox.get()))
printbtn.place(x=300, y=400)

change_theme_box = ctk.CTkSwitch(master=root1, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root1.mainloop()
