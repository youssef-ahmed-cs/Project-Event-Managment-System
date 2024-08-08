from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from CTkMessagebox import CTkMessagebox
import sqlite3
from tkinter import messagebox

def exit_app():
    root.destroy()
    os.system("python Logout.py")

def helper():
    messagebox.showinfo(title='Help',
                  message='You must choose the registration type first. If you are a user, choose User, and if you '
                          'are an Admin, select Admin. Thank you for using our application.')

def admin_login():
    root.destroy()
    os.system("python admin_Loginn.py")

def user_login():
    root.destroy()
    os.system("python User_Loginn.py")

def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

def feedback():
    def cancel():
        feedback_window.destroy()

    def show():
        text_content = text.get("0.0", END).strip()
        if not text_content:
            messagebox.showerror(title="Error", message="Please enter a message")
        else:
            save_text = text.get("0.0", END)
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO feedback (feed_back) VALUES(?)', (save_text,))
            conn.commit()
            messagebox.showinfo(title="Thanks", message="Thanks for your feedback")
            conn.close()
            text.delete("0.0", END)
            feedback_window.destroy()

    feedback_window = ctk.CTk()
    feedback_window.geometry('642x530')
    feedback_window.title("Event Management System")
    feedback_window.iconbitmap("assests/ticket_856232.ico")
    feedback_window.resizable(False, False)

    labeltext = ctk.CTkLabel(feedback_window, text='Thanks for your feedback', font=('Times New Roman', 35, 'bold'),
                             text_color='#7d9b77')
    labeltext.pack(pady=10, padx=60)

    text = ctk.CTkTextbox(feedback_window, width=600, height=400, font=('Times New Roman', 20, 'bold'), corner_radius=20,
                          scrollbar_button_color='#658f67')
    text.place(x=20, y=60)

    but_save = ctk.CTkButton(feedback_window, text='Send', font=('Times New Roman', 25, 'bold'), command=show, fg_color='#7d9b77',
                             corner_radius=20, hover_color="#9CBB9F", text_color='#120e0e')
    but_save.place(x=400, y=480)

    but_cancel = ctk.CTkButton(feedback_window, text='Cancel', font=('Times New Roman', 25, 'bold'), command=cancel,
                               fg_color='#7d9b77', hover_color="#9CBB9F", corner_radius=20, text_color='#120e0e')
    but_cancel.place(x=100, y=480)

    feedback_window.mainloop()

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
label_photo.pack()

loginFrame = ctk.CTkFrame(root, corner_radius=50, width=600, height=500, bg_color="#7b987e")
loginFrame.place(x=100, y=150)

labelText = ctk.CTkLabel(loginFrame, text_color="#7b987e", text='Log in as Admin or User', pady=10,
                         font=('Times New Roman', 30, 'bold'))
labelText.place(x=140, y=30)

admin = ImageTk.PhotoImage(file='assests/administrator.png')
image_login_as_admin = ctk.CTkLabel(loginFrame, image=admin, text='')
image_login_as_admin.place(x=120, y=180)
but_login_as_admin = ctk.CTkButton(loginFrame, text_color="#262724", hover_color="#9CBB9F", text='Admin',
                                   fg_color="#7B9976", font=('Times New Roman', 30, 'bold'), command=admin_login)
but_login_as_admin.place(x=100, y=310)

but_help = ctk.CTkButton(loginFrame, text_color="#262724", fg_color="#7B9976", hover_color="#9CBB9F",
                         text='Help', font=('Times New Roman', 20, 'bold'), command=helper)
but_help.place(x=150, y=455)
feedback_button = ctk.CTkButton(loginFrame, text_color="#262724", fg_color="#7B9976", hover_color="#9CBB9F",
                                text='Feedback', font=('Times New Roman', 20, 'bold'), command=feedback)
feedback_button.place(x=310, y=455)

users = ImageTk.PhotoImage(file='assests/users.png')
image_login_as_user = ctk.CTkLabel(loginFrame, width=0, height=0, image=users, text='')
image_login_as_user.place(x=400, y=190)

but_login_as_user = ctk.CTkButton(loginFrame, text_color="#262724", fg_color="#7B9976", hover_color="#9CBB9F",
                                  text='User', font=('Times New Roman', 30, 'bold'), command=user_login)
but_login_as_user.place(x=380, y=310)
but_exit = ctk.CTkButton(loginFrame, text_color="#262724", fg_color="#7B9976", hover_color="#9CBB9F",
                         text='Exit App', font=('Times New Roman', 20, 'bold'), command=exit_app, compound="left")
but_exit.place(x=240, y=380)

change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724', fg_color='#262724',
                                 font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root.mainloop()
