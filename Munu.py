import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Menu", font=("Times New Romans", 40))
label.pack(padx=0, pady=20)
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, width=5,text="order", font= ("Arial Narrow", 20))
button.pack()
root.mainloop()
