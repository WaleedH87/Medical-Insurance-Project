import os
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, Text
from tkinter.messagebox import showinfo

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('1920x1080')
root.title('Medical Insurance Calculator V5.0')

name = tk.StringVar()
age = tk.StringVar()
sex = tk.StringVar()
bmi = tk.StringVar()
kids = tk.StringVar()
smoker = tk.StringVar()


def estimate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
    
    name = name.get()
    age = age.get()
    sex = sex.get()
    bmi = bmi.get()
    num_of_children = kids.get()
    smoker = smoker.get()
    
    if sex.lower() == 'male':
        sex = 1
    else: sex = 0
    
    if smoker.lower() == 'yes':
        smoker = 1
    else: smoker = 0
    
    estimated_cost = round(250 * int(age) - 128 * sex + 370 * float(bmi) + 425 * int(num_of_children) + 24000 * smoker - 12500, 2)
    monthly = round((estimated_cost / 12) * 1.0675, 2)
    quote = f"\n{name}, your estimated medical insurance cost is £{estimated_cost} annually or £{monthly} monthly (subject to 6.75% APR)"
    showinfo(
        title='Quote',
        message=quote
    )

frame = ctk.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

buttonfont = ctk.CTkFont(family='Bahnschrift', size=24, weight='bold')

label = ctk.CTkLabel(master=frame, text='Welcome to the Medical Insurance Calculator V4.0 by Waleed H', font=('Bahnschrift', 24))
label.pack(pady=30, padx=10)

label = ctk.CTkLabel(master=frame, text='What is your full name?', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, textvariable=name, width=300, height=25)
entry1.pack(pady=12, padx=10)
name = entry1.cget('textvariable')

label = ctk.CTkLabel(master=frame, text='What is your age?', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, textvariable=age, width=125, height=25)
entry2.pack(pady=12, padx=10)
age = entry2.cget('textvariable')

label = ctk.CTkLabel(master=frame, text='What gender were you assigned at birth?', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry3 = ctk.CTkEntry(master=frame, textvariable=sex, width=200, height=25)
entry3.pack(pady=12, padx=10)
sex = entry3.cget('textvariable')

label = ctk.CTkLabel(master=frame, text='What is your BMI?\n(You can calculate this on the NHS website @ https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/) ', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry4 = ctk.CTkEntry(master=frame, textvariable=bmi, width=125, height=25)
entry4.pack(pady=12, padx=10)
bmi = entry4.cget('textvariable')

label = ctk.CTkLabel(master=frame, text='Do you smoke?', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry5 = ctk.CTkEntry(master=frame, textvariable=smoker, width=200, height=25)
entry5.pack(pady=12, padx=10)
smoker = entry5.cget('textvariable')

label = ctk.CTkLabel(master=frame, text='How many children do you have?', font=('Bahnschrift', 18))
label.pack(pady=12, padx=10)

entry6 = ctk.CTkEntry(master=frame, textvariable=kids, width=125, height=25)
entry6.pack(pady=12, padx=10)
kids = entry6.cget('textvariable')


label = ctk.CTkLabel(master=frame, text='Press submit to see your insurance estimate', font=('Bahnschrift', 18))
label.pack(pady=50, padx=10)

print(name.get())

button = ctk.CTkButton(master=frame, text='Submit', command=lambda: estimate_insurance_cost(name,age,sex,bmi,num_of_children=kids,smoker=smoker))
button.pack(pady=12, padx=10)


root.mainloop()