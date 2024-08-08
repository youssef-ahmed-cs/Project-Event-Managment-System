from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os

def back_to_main_window():
    root.destroy()
    os.system("python login_as.py")


root = ctk.CTk()

ctk.set_appearance_mode('system')
root.title('Event management system')
root.iconbitmap('assests/ticket_856232.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
img1 = ImageTk.PhotoImage(Image.open('assests/splash.png'))
label_photo = Label(root, image=img1)
label_photo.pack()
root.after(3000, back_to_main_window)
root.mainloop()
