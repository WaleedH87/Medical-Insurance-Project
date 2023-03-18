import customtkinter as ctk
import tkinter as tk
from tkinter.messagebox import showinfo

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('500x350')
root.title('LoginSys')

username = tk.StringVar()
password = tk.StringVar()

def login():
    msg = 'Welcome ' + username.get() + '! \nYour Balance: £995.95'
    showinfo(
        title='Balance',
        message=msg
    )


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login System')
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, textvariable=username)
entry1.pack(pady=12, padx=10)
username = entry1.cget('textvariable')



entry2 = ctk.CTkEntry(master=frame, textvariable=password, show='*')
entry2.pack(pady=12, padx=10)



button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

root.mainloop()
