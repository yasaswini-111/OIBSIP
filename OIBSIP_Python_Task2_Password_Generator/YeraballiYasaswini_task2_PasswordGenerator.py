import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------------- Functions ---------------------- #

def generate_password():

    try:

        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error","Password length must be greater than 0.")
            return

        exclude = exclude_entry.get()

        selected_sets = []

        if uppercase_var.get():
            chars = "".join(c for c in string.ascii_uppercase if c not in exclude)
            if chars:
                selected_sets.append(chars)

        if lowercase_var.get():
            chars = "".join(c for c in string.ascii_lowercase if c not in exclude)
            if chars:
                selected_sets.append(chars)

        if numbers_var.get():
            chars = "".join(c for c in string.digits if c not in exclude)
            if chars:
                selected_sets.append(chars)

        if symbols_var.get():
            chars = "".join(c for c in string.punctuation if c not in exclude)
            if chars:
                selected_sets.append(chars)

        if len(selected_sets) == 0:
            messagebox.showwarning("Warning","Select at least one character type.")
            return

        if length < len(selected_sets):
            messagebox.showerror(
                "Error",
                "Password length is too short for the selected options."
            )
            return

        password = []

        # Guarantee one character from every selected set
        for s in selected_sets:
            password.append(random.choice(s))

        all_characters = "".join(selected_sets)

        while len(password) < length:
            password.append(random.choice(all_characters))

        random.shuffle(password)

        password = "".join(password)

        password_entry.config(state="normal")
        password_entry.delete(0,tk.END)
        password_entry.insert(0,password)
        password_entry.config(state="readonly")

        # Better Strength Calculation

        score = 0

        if length >= 8:
            score += 1

        if length >= 12:
            score += 1

        if uppercase_var.get():
            score += 1

        if lowercase_var.get():
            score += 1

        if numbers_var.get():
            score += 1

        if symbols_var.get():
            score += 1

        if score <= 3:
            strength = "Weak"
            colour = "red"

        elif score <=5:
            strength = "Medium"
            colour = "orange"

        else:
            strength = "Strong"
            colour = "green"

        strength_label.config(
            text=f"Password Strength : {strength}",
            fg=colour
        )

    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid password length.")

def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Success", "Password copied successfully!")


def clear_fields():

    length_entry.delete(0, tk.END)

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    strength_label.config(text="")

    uppercase_var.set(True)
    lowercase_var.set(True)
    numbers_var.set(True)
    symbols_var.set(True)


# ---------------------- Window ---------------------- #

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x470")
root.resizable(False, False)

root.configure(bg="#F7E8FF")

# ---------------------- Heading ---------------------- #

heading = tk.Label(
    root,
    text=" RANDOM PASSWORD GENERATOR",
    font=("Arial",17,"bold"),
    bg="#F7E8FF",
    fg="#7B2CBF"
)

heading.pack(pady=10)

# ---------------------- Length ---------------------- #

length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12, "bold"),
    bg="#F7E8FF",
    fg="#3A86FF"
)

length_label.pack()

length_entry = tk.Entry(
    root,
    width=12,
    justify="center",
    font=("Arial", 14),
    bd=3
)

length_entry.pack(pady=5)

exclude_label = tk.Label(
    root,
    text="Exclude Characters (Optional)",
    font=("Arial",11,"bold"),
    bg="#F7E8FF",
    fg="#3A86FF"
)

exclude_label.pack()

exclude_entry = tk.Entry(
    root,
    width=18,
    justify="center",
    font=("Arial",12),
    bd=2
)

exclude_entry.pack(pady=5)

# ---------------------- Options ---------------------- #

options_frame = tk.Frame(root, bg="#F7E8FF")
options_frame.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    options_frame,
    text="Uppercase Letters",
    variable=uppercase_var,
    bg="#F7E8FF",
    font=("Arial",11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Lowercase Letters",
    variable=lowercase_var,
    bg="#F7E8FF",
    font=("Arial",11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Numbers",
    variable=numbers_var,
    bg="#F7E8FF",
    font=("Arial",11)
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Special Symbols",
    variable=symbols_var,
    bg="#F7E8FF",
    font=("Arial",11)
).pack(anchor="w")

# ---------------------- Generate Button ---------------------- #

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial",12,"bold"),
    bg="#FF66C4",
    fg="white",
    width=20,
    relief="raised",
    bd=3
)

generate_btn.pack(pady=10)

# ---------------------- Password ---------------------- #

password_entry = tk.Entry(
    root,
    width=35,
    font=("Consolas",13),
    justify="center",
    state="readonly",
    bd=3
)

password_entry.pack()

# ---------------------- Strength ---------------------- #

strength_label = tk.Label(
    root,
    text="",
    font=("Arial",12,"bold"),
    bg="#F7E8FF"
)

strength_label.pack(pady=8)

# ---------------------- Buttons ---------------------- #

button_frame = tk.Frame(root,bg="#F7E8FF")
button_frame.pack()

copy_btn = tk.Button(
    button_frame,
    text=" Copy",
    command=copy_password,
    bg="#3A86FF",
    fg="white",
    width=12,
    font=("Arial",11,"bold")
)

copy_btn.grid(row=0,column=0,padx=15)

clear_btn = tk.Button(
    button_frame,
    text=" Clear",
    command=clear_fields,
    bg="#8338EC",
    fg="white",
    width=12,
    font=("Arial",11,"bold")
)

clear_btn.grid(row=0,column=1,padx=15)


root.mainloop()