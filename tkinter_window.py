import tkinter as tk
from tkinter import messagebox

def submit_action():
    selections = [
        listbox1.get(tk.ACTIVE),
        listbox2.get(tk.ACTIVE),
        listbox3.get(tk.ACTIVE),
    ]
    checkbox_value = checkbox_var.get()
    message = f"Selections:\nList 1: {selections[0]}\nList 2: {selections[1]}\nList 3: {selections[2]}\nCheckbox checked: {checkbox_value}"
    messagebox.showinfo("Submission Result", message)

root = tk.Tk()
root.title("Cludeo Calculator")
root.geometry("400x400")

person = ["Person1", "Person2", "Person3"]
våpen = ["Våpen1", "Våpen2", "Våpen3"]
sted = ["Sted1", "Sted2", "Sted3"]

listbox1 = tk.Listbox(root)
listbox2 = tk.Listbox(root)
listbox3 = tk.Listbox(root)

for item in person:
    listbox1.insert(tk.END, item)
for item in våpen:
    listbox2.insert(tk.END, item)
for item in sted:
    listbox3.insert(tk.END, item)

listbox1.pack(pady=5)
listbox2.pack(pady=5)
listbox3.pack(pady=5)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Fikk spiller se noen kort?", variable=checkbox_var)
checkbox.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack(pady=20)

root.mainloop()
