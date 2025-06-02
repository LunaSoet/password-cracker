import tkinter as tk
from tkinter import ttk, messagebox
from brute_force import brute_force
from dictionary_attack import dictionary_attack

def run_crack():
    target_hash = hash_entry.get().strip()
    algorithm = hash_type.get()
    max_len = int(length_spinbox.get())
    mode = mode_var.get()

    if not target_hash:
        messagebox.showerror("Error", "Please enter a hash.")
        return

    if mode == "Brute Force":
        result = brute_force(target_hash, algorithm=algorithm, max_length=max_len)
    else:
        result = dictionary_attack(target_hash, algorithm=algorithm)

    result_label.config(text=result)

app = tk.Tk()
app.title("Password Cracker (Ethical)")
app.geometry("500x350")
app.resizable(False, False)

tk.Label(app, text="Enter Hash to Crack:").pack(pady=5)
hash_entry = tk.Entry(app, width=60)
hash_entry.pack(pady=5)

tk.Label(app, text="Hash Algorithm:").pack()
hash_type = ttk.Combobox(app, values=["sha256", "sha1", "md5"])
hash_type.current(0)
hash_type.pack()

tk.Label(app, text="Max Length (for brute force):").pack()
length_spinbox = tk.Spinbox(app, from_=1, to=6)
length_spinbox.pack()

tk.Label(app, text="Attack Mode:").pack()
mode_var = tk.StringVar(value="Brute Force")
ttk.Combobox(app, textvariable=mode_var, values=["Brute Force", "Dictionary"]).pack()

tk.Button(app, text="Crack Password", command=run_crack).pack(pady=10)
result_label = tk.Label(app, text="", wraplength=480)
result_label.pack(pady=10)

app.mainloop()
