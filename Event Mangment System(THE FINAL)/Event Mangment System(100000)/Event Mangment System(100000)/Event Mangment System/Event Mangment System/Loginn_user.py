from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk


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
label_photo.pack()

loginFrame = ctk.CTkFrame(root, corner_radius=50, width=600, height=500, bg_color='#7E9779')
loginFrame.place(x=100, y=150)

labelText = ctk.CTkLabel(loginFrame, text_color="#7b987e", text='Log in as Admin or User', pady=10,
                         font=('Times New Roman', 30, 'bold'))
labelText.place(x=140, y=10)

admin = ImageTk.PhotoImage(file='assests/administrator.png')
image_login_as_admin = ctk.CTkLabel(loginFrame, image=admin, text='')
image_login_as_admin.place(x=120, y=180)
but_login_as_admin = ctk.CTkButton(loginFrame, text_color="#262724", hover_color="#7B9976", text='Admin',
                                   fg_color="#7B9976", font=('Times New Roman', 30, 'bold'), )
but_login_as_admin.place(x=100, y=310)

helps = ImageTk.PhotoImage(file='assests/help (2).png')
but_help = ctk.CTkButton(loginFrame, image=helps, text_color="#262724", fg_color="#7B9976", hover_color="#7B9976",
                         text='Help', font=('Times New Roman', 20, 'bold'))
but_help.place(x=230, y=455)

users = ImageTk.PhotoImage(file='assests/users.png')
image_login_as_admin = ctk.CTkLabel(loginFrame, width=0, height=0, image=users, text='')
image_login_as_admin.place(x=400, y=190)

but_login_as_user = ctk.CTkButton(loginFrame, text_color="#262724", fg_color="#7B9976", hover_color="#7B9976",
                                  text='User', font=('Times New Roman', 30, 'bold'), )
but_login_as_user.place(x=380, y=310)

change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724', fg_color='#262724',
                                 font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root.mainloop()
