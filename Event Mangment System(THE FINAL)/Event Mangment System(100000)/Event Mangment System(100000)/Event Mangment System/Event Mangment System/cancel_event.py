import tkinter as tk
from tkinter import ttk
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image, ImageTk
import os
import customtkinter as ctk

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Function to add an event
def add_event():
    print("Add Event button clicked")
    if not (event_id_text.get() and event_name_text.get() and event_date_text.get() and event_time_text.get() and event_duration_text.get()):
        CTkMessagebox(title="❌ Error", message="Enter valid inputs", button_color="#7B9976", button_hover_color="#7B9976",
                      bg_color="#262724", font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976",
                      title_color="#7B9976", option_1="OK", button_text_color="#262724")
        return
    try:
        cur.execute("INSERT INTO Event (event_id, event_name, event_date, event_time, event_duration) VALUES (?, ?, ?, ?, ?)",
                    (event_id_text.get(), event_name_text.get(), event_date_text.get(), event_time_text.get(), event_duration_text.get()))
        conn.commit()
        clear_inputs()
        fetch_data()
    except sqlite3.IntegrityError:
        CTkMessagebox(title="❌ Error", message="Event name must be unique", button_color="#7B9976", button_hover_color="#7B9976",
                      bg_color="#262724", font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976",
                      title_color="#7B9976", option_1="OK", button_text_color="#262724")

# Function to update an event
def update_event():
    print("Update Event button clicked")
    if event_name_text.get() == '':
        CTkMessagebox(title="❌ Error", message="Select an Event from the table and click 'Get Selected Data' button to Update",
                      button_color="#7B9976", button_hover_color="#7B9976", bg_color="#262724",
                      font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976",
                      title_color="#7B9976", option_1="OK", button_text_color="#262724")
        return
    print("Updating event with name:", event_name_text.get())
    print("New values:", event_id_text.get(), event_date_text.get(), event_time_text.get(), event_duration_text.get())
    cur.execute("UPDATE Event SET event_id = ?, event_date = ?, event_time = ?, event_duration = ? WHERE event_name = ?",
                (event_id_text.get(), event_date_text.get(), event_time_text.get(), event_duration_text.get(), event_name_text.get()))
    conn.commit()
    clear_inputs()
    fetch_data()

# Function to delete an event
def delete_event():
    print("Delete Event button clicked")
    if not event_name_text.get():
        CTkMessagebox(title="❌ Error", message="Select an event from the table and click 'Get Selected Event' button to delete",
                      button_color="#7B9976", button_hover_color="#7B9976", bg_color="#262724", font=('Times New Roman', 15, 'bold'),
                      icon="warning", fg_color="#7B9976", title_color="#7B9976", option_1="OK", button_text_color="#262724")
        return
    print("Deleting event with name:", event_name_text.get())
    cur.execute("DELETE FROM Event WHERE event_name=?", (event_name_text.get(),))
    conn.commit()
    clear_inputs()
    fetch_data()

# Function to fetch data from the database
def fetch_data():
    print("Fetch data from the database")
    cur.execute("SELECT * FROM Event")
    rows = cur.fetchall()
    clear_table()
    for row in rows:
        table_tree.insert("", "end", values=row)
    print("Fetched data:", rows)

# Function to clear the table
def clear_table():
    for item in table_tree.get_children():
        table_tree.delete(item)

# Function to clear input fields
def clear_inputs():
    event_id_text.set("")
    event_name_text.set("")
    event_date_text.set("")
    event_time_text.set("")
    event_duration_text.set("")

# Function to get selected data from the table
def get_selected_data():
    print("Get Selected Event button clicked")
    selected_item = table_tree.selection()
    if selected_item:
        selected_data = table_tree.item(selected_item[0], 'values')
        print("Selected data:", selected_data)
        event_id_text.set(selected_data[1])
        event_name_text.set(selected_data[0])
        event_date_text.set(selected_data[2])
        event_time_text.set(selected_data[3])
        event_duration_text.set(selected_data[4])

# Initialize main window
Emp_page = CTk()
Emp_page.title('Event Management System')
Emp_page.iconbitmap('assests/ticket_856232.ico')
screen_width = Emp_page.winfo_screenwidth()
screen_height = Emp_page.winfo_screenheight()
center_x = 0
center_y = 0
Emp_page.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
#Emp_page.config(bg="#7b987e")
my_app_Color = "#262724"
Emp_page.config(bg=my_app_Color)

# Title
page_title = CTkLabel(Emp_page, text='Admin Edit', font=('Times New Roman', 50, 'bold'), text_color='#7B9976',bg_color="#262724")
page_title.pack(pady=20)

# Frame for Table
table_frame = CTkFrame(Emp_page, fg_color="#7B9976",width=400,height=600)
table_frame.place(x=580,y=160)

# Table
table_columns = ['Event Name', 'Event ID', 'Event Date', 'Event Time', 'Event Duration']
table_tree = ttk.Treeview(table_frame, columns=table_columns, show="headings", selectmode="browse", height=20)
table_tree.pack(side="left", fill="both", expand=True)

for col in table_columns:
    table_tree.heading(col, text=col)
    table_tree.column(col, anchor="center")

# Scrollbar for Table
scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table_tree.yview)
scrollbar.pack(side="right", fill="y")
table_tree.configure(yscroll=scrollbar.set)

# Frame for Input Fields
input_frame = CTkFrame(Emp_page, fg_color="#262724")
input_frame.place(x=100,y=200)

# Input Fields
labels = ["Event Name", "Event ID", "Event Date", "Event Time", "Event Duration"]
entries = []
for i, label in enumerate(labels):
    CTkLabel(input_frame, text=label, font=('Times New Roman', 20, 'bold'), fg_color='#262724', text_color='white').grid(row=i, column=0, padx=10, pady=10, sticky='w')
    entry = CTkEntry(input_frame, width=200, height=30, font=('Times New Roman', 20, 'bold'), bg_color='#262724', corner_radius=15)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries.append(entry)

event_name_text, event_id_text, event_date_text, event_time_text, event_duration_text = [tk.StringVar() for _ in entries]

for entry, text_var in zip(entries, [event_name_text, event_id_text, event_date_text, event_time_text, event_duration_text]):
    entry.configure(textvariable=text_var)

# Frame for Buttons
button_frame = CTkFrame(Emp_page, fg_color="#262724")
button_frame.place(x=350,y=600)

# Buttons
buttons = [
    ("Add Event", add_event),
    ("Update Event", update_event),
    ("Delete Event", delete_event),
    ("Get Selected Event", get_selected_data)
]

for i, (btn_text, btn_command) in enumerate(buttons):
    CTkButton(button_frame, text=btn_text, command=btn_command, font=('Times New Roman', 20, 'bold'),
              fg_color='#7d9b77', hover_color="#9CBB9F", text_color='#262724', corner_radius=15,
              bg_color='#262724').grid(row=0, column=i, padx=20, pady=10)

# Fetch Data on Start
fetch_data()

def back():
    Emp_page.destroy()
    os.system("python adminpage.py")

def clear_input():
    event_id_text.set("")
    event_name_text.set("")
    event_date_text.set("")
    event_duration_text.set("")
    event_time_text.set("")

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
# but_back = ctk.CTkButton(Emp_page, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9B75', command=back)
# but_back.place(x=20, y=20)
but_back = ctk.CTkButton(Emp_page, text='', fg_color='#262724', hover_color='#7B9976', image=back_image, width=40,
                         command=back)
but_back.place(x=20, y=20)
table_style = ttk.Style()
table_style.configure("Treeview" ,font=('Times New Roman', 11) , rowheight = 20 , foreground = "#262724" , background = "#7d9b77")
table_style.map("Treeview" , foreground = [("selected" , "white")] , background = [("selected" , "#262724")])
table_style.configure('Treeview.Heading',font=('Times New Roman',15,'bold'),background='#7d9b77', foreground='#262724',)
for i in table_columns:
  table_tree.heading(i , text=i)
# Run the main loop
Emp_page.mainloop()
