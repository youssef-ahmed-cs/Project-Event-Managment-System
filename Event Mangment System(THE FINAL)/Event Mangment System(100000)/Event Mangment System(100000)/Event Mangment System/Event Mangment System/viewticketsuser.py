import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sqlite3

from PIL import ImageTk
from customtkinter import *
from CTkMessagebox import CTkMessagebox

Emp_page = CTk()
sw = Emp_page.winfo_screenwidth()
sh = Emp_page.winfo_screenheight()
center_x = 0
center_y = 0
Emp_page.geometry(f"{sw}x{sh}+{center_x}+{center_y}")
Emp_page.title("Event Management System")
Emp_page.iconbitmap("assests/ticket_856232.ico")
my_app_Color = "#262724"
Emp_page.config(bg=my_app_Color)

conn = sqlite3.connect("database.db")
cur = conn.cursor()




add_btn_img = PhotoImage(file=r"assests\plus.png")
update_btn_img = PhotoImage(file=r"assests\update.png")
delete_btn_img = PhotoImage(file=r"assests\recycle-bin (1).png")


labeltext = CTkLabel(Emp_page,corner_radius=15,text='User Ticket', font=('Times New Roman', 50, 'bold'), text_color='#7B9976',bg_color="#262724")
labeltext.place(x=sw // 2 - 70 , y=110)





table_columns = ['Event ID','Event Name','Event time','Event Date','Event Duration']
table_tree = ttk.Treeview(Emp_page , columns=table_columns , show="headings" , selectmode="browse" , height=11)
table_tree.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)

table_style = ttk.Style()
table_style.configure("Treeview" ,font=('Times New Roman', 11) , rowheight = 30 , foreground = "#262724" , background = "#7d9b77")
table_style.map("Treeview" , foreground = [("selected" , "white")] , background = [("selected" , "#262724")])
table_style.configure('Treeview.Heading',font=('Times New Roman',15,'bold'),background='#7d9b77', foreground='#262724',)
for i in table_columns:
  table_tree.heading(i , text=i)



table_tree.place(x=50, y=0, width=sw-500, height=sh-450)

# ضبط عرض الأعمدة لتملأ مساحة Treeview
table_tree.column('Event ID', width=(sw-500)//4, anchor='center')
table_tree.column('Event Name', width=(sw-500)//4, anchor='center')
table_tree.column('Event time', width=(sw-500)//4, anchor='center')
table_tree.column('Event Date', width=(sw-500)//4, anchor='center')
table_tree.column('Event Duration', width=(sw-500)//4, anchor='center')

def del_selected():
    for selection in table_tree.selection():
        table_tree.delete(selection)
        conn = sqlite3.connect("database.db")

#make a scroll bar
# scrollbar = CTkScrollbar(Emp_page , orientation='vertical' , command=table_tree.yview,fg_color='#7B9976')
# table_tree.configure(yscroll=scrollbar.set)
# scrollbar.place(x=1543,y=350)
# end children
scrollbar = ttk.Scrollbar(Emp_page, orient='vertical', command=table_tree.yview)
scrollbar.place(x=1505,y=450)
table_tree.configure(yscroll=scrollbar.set)
def fetch_data():
  cur.execute("SELECT * FROM Event")
  rows = cur.fetchall()
  clear_table_tree()
  for i  in rows:
    table_tree.insert("" , "end" , values=i )

def clear_table_tree():
  for item in table_tree.get_children():
    table_tree.delete(item)

def back():
    Emp_page.destroy()
    os.system("python userpage.py")

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back =CTkButton(Emp_page, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9B75', command=back)
but_back.place(x=10, y=10)


fetch_data()
Emp_page.mainloop()
