import sqlite3
import tkinter as tk
from tkinter import ttk
from customtkinter import *
import customtkinter as ctk
import os
from PIL import Image, ImageTk

# Connect to the SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Replace 'events' with the correct table name if different
cursor.execute("SELECT event_name, event_id, event_date, event_time, event_duration FROM event")
current_user_tickets = cursor.fetchall()
conn.close()

# Function to fetch user tickets and insert them into the Treeview
def fetch_user_tickets():
    for ticket in current_user_tickets:
        table_tree.insert("", "end", values=ticket)

# Initialize main window
root = ctk.CTk()
root.title('User Tickets')
root.iconbitmap('assests/ticket_856232.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
root.config(bg="#7b987e")

# Frame for Table
table_frame = CTkFrame(root, fg_color="#7B9976", width=screen_width, height=screen_height)
table_frame.pack(fill="both", expand=True, padx=40, pady=40)

# Table
table_columns = ['Event_name', 'Event_id', 'Event_date', 'Event_time', 'Event_duration']

# Create a style and configure it
style = ttk.Style()
style.configure("Treeview.Heading", font=("Times New Roman", 16, "bold"))
style.configure("Treeview", font=("Times New Roman", 14))

table_tree = ttk.Treeview(table_frame, columns=table_columns, show="headings", selectmode="browse", style="Treeview")
table_tree.pack(side="left", fill="both", expand=True)

for col in table_columns:
    table_tree.heading(col, text=col)
    table_tree.column(col, anchor="center")

# Scrollbar for Table
scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table_tree.yview)
scrollbar.pack(side="right", fill="y")
table_tree.configure(yscroll=scrollbar.set)

# Fetch Data on Start
fetch_user_tickets()

# Function to handle the back button action
# def back():
#     root.destroy()
#     os.system("python userpage.py")
#
# back_image = ImageTk.PhotoImage(file='assests/backspace.png')
# but_back = ctk.CTkButton(root, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9B75', command=back)
# but_back.place(x=10, y=10)

# Run the main loop
root.mainloop()
