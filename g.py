import tkinter as tk
root = tk.Tk()
root.title("Student registrtion")

name_label = tk.Label(root,text = "Enter name")
name_label.pack()

name_textbox = tk.Entry(root)
name_textbox.pack()

label = tk.Label(root,text = "Enter email")
label.pack()

phone = tk.Label(root,text = "Enter phone number")
phone.pack()

phone_t = tk.Entry(root)
phone_t.pack()


