import tkinter as tk
from tkinter import messagebox

def start_fake_ddos():
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address.")
        return
    messagebox.showinfo("Skid", "Please go outside and touch grass")

root = tk.Tk()
root.title("DDoS attack")
root.geometry("400x250")

ip_label = tk.Label(root, text="Enter IP address:")
ip_label.pack(pady=(20, 5))

ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_fake_ddos)
start_button.pack(pady=10)

root.mainloop()




































#