import customtkinter as ctk
import CTkMessagebox
from CTkMessagebox import CTkMessagebox

root = ctk.CTk()
root.title("Login")
root.configure(bg='#345345')
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

def login():
    username = "Ray"
    password = "1234"
    if entry.get() == username and entry1.get() == password:
        root.quit() 
        bank_app = ctk.CTk
        ctk.set_appearance_mode("dark")
    elif entry.get() == username and entry1.get() != password: 
        CTkMessagebox(title='Wrong password',message='Please check your password') 
    elif entry.get() == username and entry1.get() != password: 
        CTkMessagebox(title='Wrong username',message='Please check your username') 
    else: 
        CTkMessagebox(title="Login Failed",message="Invalid Username and password")
    bank_app.mainloop()             

label = ctk.CTkLabel(root, text="Username")
label.pack(side='top', anchor='center', pady=5)
label.pack()

entry = ctk.CTkEntry(root)
entry.pack(side='top', anchor='center', pady=5)
entry.pack()

label = ctk.CTkLabel(root, text="Password")
label.pack(side='top', anchor='center', pady=5)
label.pack()

entry1 = ctk.CTkEntry(root)
entry1.pack(side='top', anchor='center', pady=5)
entry1.pack()

button = ctk.CTkButton(root, text="login", command=login)
button.pack(side='top', anchor='center', pady=5)
button.pack()

root.mainloop()
