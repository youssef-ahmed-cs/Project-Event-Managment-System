import tkinter as tk
from tkinter import ttk
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import customtkinter as ctk
# Read the username from the temporary file
try:
    with open("current_user.txt", "r") as file:
        current_user = file.read().strip()
except FileNotFoundError:
    print("current_user.txt file not found. Make sure to log in first.")
    messagebox.showerror(title="Error", message="No user logged in. Please log in first")

    exit()  # Exit the script if no user is logged in

conn = sqlite3.connect("database.db")
cur = conn.cursor()

def fetch_data():
    print("Fetch data from the database")
    print(current_user)
    cur.execute("SELECT * FROM ticket WHERE user_name1=?", (current_user,))
    rows = cur.fetchall()
    clear_table()
    for row in rows:
        table_tree.insert("", "end", values=row)
    print("Fetched data:", rows)

def clear_table():
    for item in table_tree.get_children():
        table_tree.delete(item)

def delete_selected():
    selected_item = table_tree.selection()
    if selected_item:
        item = table_tree.item(selected_item)
        values = item['values']
        ticket_id = values[0]
        try:
            cur.execute("DELETE FROM ticket WHERE ticket_id=?", (ticket_id,))
            conn.commit()
            table_tree.delete(selected_item)
            messagebox.showinfo(title="Success", message="Ticket deleted successfully.")

        except sqlite3.Error as error:
            print("Failed to delete ticket:", error)
            messagebox.showerror(title="Error", message="Failed to delete ticket.")
    else:
        messagebox.showerror(title="Error", message="No ticket selected.")

Emp_page = CTk()
Emp_page.title('Event Management System')
Emp_page.iconbitmap('assests/ticket_856232.ico')
screen_width = Emp_page.winfo_screenwidth()
screen_height = Emp_page.winfo_screenheight()
center_x = 0
center_y = 0
Emp_page.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
Emp_page.config(bg="#262724")

page_title = CTkLabel(Emp_page, text='Cancel Ticket',  font=('Times New Roman', 50, 'bold'), text_color='#7B9976',bg_color="#262724")
page_title.pack(pady=20)

table_frame = CTkFrame(Emp_page, fg_color="#7B9976", width=800, height=800)
table_frame.place(relx=0.5, rely=0.4,anchor=tk.CENTER)
#table_frame.place(x=320, y=130)
table_columns = ['Ticket ID', 'Username', 'Event name']
table_tree = ttk.Treeview(table_frame, columns=table_columns, show="headings", selectmode="browse", height=18)
table_tree.pack(side="left", fill="both", expand=True)

for col in table_columns:
    table_tree.heading(col, text=col)
    table_tree.column(col, anchor="center",width=400)

scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=table_tree.yview)
scrollbar.pack(side="right", fill="y")
table_tree.configure(yscroll=scrollbar.set)

button_frame = CTkFrame(Emp_page, fg_color="#262724")
button_frame.place(x=650, y=600)

# Add Delete button
delete_button = CTkButton(button_frame, text='Delete Ticket', font=('Times New Roman', 30, 'bold'), fg_color="#7B9976",corner_radius=15,
                          hover_color="#9CBB9F", text_color='#262724', command=delete_selected)
delete_button.grid(row=0, column=0, padx=20, pady=10)

fetch_data()

def back():
    Emp_page.destroy()
    os.system("python userpage.py")

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(Emp_page, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9B75', command=back)
but_back.place(x=20, y=20)
table_style = ttk.Style()
table_style.configure("Treeview" ,font=('Times New Roman', 11) , rowheight = 30 , foreground = "#262724" , background = "#7d9b77")
table_style.map("Treeview" , foreground = [("selected" , "white")] , background = [("selected" , "#262724")])
table_style.configure('Treeview.Heading',font=('Times New Roman',15,'bold'),background='#7d9b77', foreground='#262724',)
for i in table_columns:
  table_tree.heading(i , text=i)
Emp_page.mainloop()
