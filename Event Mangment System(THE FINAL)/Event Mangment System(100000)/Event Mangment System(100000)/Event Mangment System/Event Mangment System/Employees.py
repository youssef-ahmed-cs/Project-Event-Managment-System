import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sqlite3
from customtkinter import *
from CTkMessagebox import  CTkMessagebox

Emp_page = CTk()
sw= Emp_page.winfo_screenwidth()
sh = Emp_page.winfo_screenheight()
Emp_page.geometry(f"{sw}x{sh}")
Emp_page.title("Admin page")
my_app_Color="#7B9976"
Emp_page.config(bg=my_app_Color)

conn = sqlite3.connect("database.db")
cur = conn.cursor()

def add_emp():
  if entryid.get() =='' or entryTime.get() =='' or  entrydate.get() =='' or  entryname.get() =='' or  entryduration.get() =='' :
    CTkMessagebox(title="❌ error" ,message= "Enter Valid inputs")
    return
  cur.execute("INSERT INTO Event (event_id,event_name,event_date,event_time,event_duration) VALUES (?,?,?,?,?)" , (event_id_text.get() ,event_name_text.get() , event_date_text.get() , event_time_text.get() , event_dur_text.get()))
  conn.commit()
  clear_input()
  fetch_data()


def update_emp():
  if event_id_text.get() == '':
    CTkMessagebox(title="❌ error" ,message= "Select an Event from table and click 'Get Selected Data' button to Update")
  cur.execute("UPDATE Event SET event_id = ? , event_name = ? , event_date = ? , event_time = ? , event_duration = ?" , (event_id_text.get() ,event_name_text.get() , event_date_text.get() , event_time_text.get() , event_dur_text.get() ))
  conn.commit()
  clear_input()
  fetch_data()

def delete_emp():
  if event_id_text.get() == '':
    CTkMessagebox(title="❌ error" ,message= "Select an Event from table and click 'Get Selected Data' button to Delete")
  cur.execute("DELETE FROM Event WHERE event_id = ?",(event_id_text.get() , ))
  conn.commit()
  clear_input()
  fetch_data()

#

for widget in Emp_page.winfo_children():
  widget.grid_configure(padx=5 , pady=12)

add_btn_img = PhotoImage(file="assests\\add.png")
update_btn_img = PhotoImage(file=r"assests\update.png")
delete_btn_img = PhotoImage(file=r"assests\delete.png")
CTkButton(Emp_page , text=" Add Event  ",corner_radius=15 , command=add_emp  , image = add_btn_img ,font=('Times New Roman', 20, 'bold'), compound="right",bg_color='#7B9976').place(x=50,y=600)
CTkButton(Emp_page , text=" Update Event  ",corner_radius=15 , command=update_emp  , image = update_btn_img,font=('Times New Roman', 20, 'bold') , compound="right",bg_color='#7B9976').place(x=50,y=700)
CTkButton(Emp_page , text=" Delete Event  " ,corner_radius=15 ,command=delete_emp  , image = delete_btn_img,font=('Times New Roman', 20, 'bold') , compound="right",bg_color='#7B9976').place(x=50,y=800)

# emp_data_frame
page_title = CTkLabel(Emp_page,text='Admin edit',bg_color='#7B9976',font=('Times New Roman', 45, 'bold'))
page_title.place(x=850,y=20)

labelname = CTkLabel(Emp_page,text='Event Name',pady=10 ,font=('Times New Roman',30, 'bold'),bg_color='#7B9976')
labelname.place(x = 40 , y = 120)

labelid = CTkLabel(Emp_page,text='Event ID',pady=10 ,font=('Times New Roman',30, 'bold'),bg_color='#7B9976')
labelid.place(x = 40 , y = 190)

labeldate = CTkLabel(Emp_page,text='Event Date',pady=10 ,font=('Times New Roman', 30, 'bold'),bg_color='#7B9976')
labeldate.place(x = 40 , y = 260)

labelTime = CTkLabel(Emp_page,text='Event Time',pady=10 ,font=('Times New Roman', 30, 'bold'),bg_color='#7B9976')
labelTime.place(x = 40 , y = 330)

labelduration = CTkLabel(Emp_page,text='Event Duration',pady=10 ,font=('Times New Roman', 30, 'bold'),bg_color='#7B9976')
labelduration.place(x = 40 , y = 400)

table_data_frame = CTkFrame(Emp_page,fg_color='#7B9976' )
table_data_frame.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)

event_name_text = StringVar()
entryname = CTkEntry(Emp_page, width=200, height=30,font=('Times New Roman', 20, 'bold'),bg_color='#7B9976',corner_radius=15,textvariable=event_name_text)
entryname.place(x = 250 , y = 135)

event_id_text = StringVar()
entryid = CTkEntry(Emp_page, width=200, height=30,font=('Times New Roman',20, 'bold'),bg_color='#7B9976',corner_radius=15,textvariable=event_id_text)
entryid.place(x = 250 , y = 200)


event_date_text = StringVar()
entrydate = CTkEntry(Emp_page,width=200, height=30,font=('Times New Roman', 20, 'bold'),bg_color='#7B9976',corner_radius=15,textvariable=event_date_text)
entrydate.place(x = 250 , y = 275)

event_time_text = StringVar()
entryTime = CTkEntry(Emp_page,width=200, height=30,font=('Times New Roman', 20, 'bold'),bg_color='#7B9976',corner_radius=15,textvariable=event_time_text)
entryTime.place(x = 250 , y = 345)

event_dur_text = StringVar()
entryduration = CTkEntry(Emp_page ,width=200, height=30,font=('Times New Roman', 20, 'bold'),bg_color='#7B9976',corner_radius=15,textvariable=event_dur_text)
entryduration.place(x = 250 , y = 415)

# start children of table_data_frame

table_columns = ['Event ID','Event Name','Event time','Event Date','Event Duration']
table_tree = ttk.Treeview(Emp_page , columns=table_columns , show="headings" , selectmode="browse" , height=11)
table_tree.place(x=600,y=200)

table_style = ttk.Style()
table_style.configure("Treeview" ,font=('Times New Roman', 10) , rowheight = 40 , foreground = "black" , background = "#e2e2e2")
table_style.map("Treeview" , foreground = [("selected" , "white")] , background = [("selected" , "#743e3a")])

for i in table_columns:
  table_tree.heading(i , text=i)




table_tree.column("Event ID" , width=90 , anchor="center" )
table_tree.column("Event Name" , width=140 )
table_tree.column("Event time" , width=120 , anchor="center")
table_tree.column("Event Date" , width=140)
table_tree.column("Event Duration" , width=170 , anchor="center")

def get_selected_data():
  for selected_item in table_tree.selection():
    event_id_text.set(table_tree.item(selected_item)["values"][0])
    event_name_text.set(table_tree.item(selected_item)["values"][1])
    event_time_text.set(table_tree.item(selected_item)["values"][2])
    event_date_text.set(table_tree.item(selected_item)["values"][3])
    event_dur_text.set(table_tree.item(selected_item)["values"][4])
    print(table_tree.item(selected_item)["values"])

CTkButton(Emp_page , text=" Get Selected Event "  , command=get_selected_data,font=('Times New Roman', 30, 'bold'),corner_radius=15,bg_color='#7B9976' ).place(x=800,y=700)

#make a scroll bar
scrollbar = CTkScrollbar(table_data_frame , orientation='vertical' , command=table_tree.yview)
table_tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0 , column=1 , sticky="NS" )
# end children
def fetch_data():
  cur.execute("SELECT * FROM Event")
  rows = cur.fetchall()
  clear_table_tree()
  for i  in rows:
    table_tree.insert("" , "end" , values=i )

# Function to clear all data from the Treeview
def clear_table_tree():
  for item in table_tree.get_children():
    table_tree.delete(item)

def clear_input():
  event_id_text.set("")
  event_name_text.set("")
  event_date_text.set("")
  event_dur_text.set("")
  event_time_text.set("")

fetch_data()

Emp_page.mainloop()