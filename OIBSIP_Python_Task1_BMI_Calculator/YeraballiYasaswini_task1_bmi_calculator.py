import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
def calculate_bmi():
    

    name = name_entry.get().strip()
    gender = gender_var.get()

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Invalid Name", "Please enter a valid name.")
        return

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

                # Validate weight and height

        if weight <= 0 and height <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be greater than zero."
            )
            return

        elif weight <= 0:
            messagebox.showerror(
                "Invalid Weight",
                "Weight must be greater than zero."
            )
            return

        elif height <= 0:
            messagebox.showerror(
                "Invalid Height",
                "Height must be greater than zero."
            )
            return

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
        return

    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
        tip = "Eat a healthy and balanced diet."

    elif bmi < 25:
        category = "Normal Weight"
        tip = "Great! Keep maintaining your healthy lifestyle."

    elif bmi < 30:
        category = "Overweight"
        tip = "Exercise regularly and reduce junk food."

    else:
        category = "Obese"
        tip = "Consult a healthcare professional."

    ideal_min = round(18.5 * (height ** 2), 2)
    ideal_max = round(24.9 * (height ** 2), 2)

    save_data(name, gender, weight, height, bmi, category)

    bmi_label.config(text=f"BMI : {bmi}")

    if category == "Underweight":
        colour = "blue"
        score = 60

    elif category == "Normal Weight":
        colour = "green"
        score = 95

    elif category == "Overweight":
        colour = "orange"
        score = 75

    else:
        colour = "red"
        score = 45

    category_label.config(
        text=f"Category : {category}",
        fg=colour
    )

    tip_label.config(
        text=f"Health Tip : {tip}"
    )

    ideal_label.config(
        text=f"Ideal Weight : {ideal_min} kg - {ideal_max} kg"
    )

    score_label.config(
        text=f"Health Score : {score}/100"
    )
def view_history():

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("700x400")
    history_window.configure(bg="#F8E8FF")

    title = tk.Label(
        history_window,
        text="BMI History",
        font=("Arial", 18, "bold"),
        bg="#F8E8FF",
        fg="#7B2CBF"
    )
    title.pack(pady=10)

    text = tk.Text(
        history_window,
        width=80,
        height=18,
        font=("Consolas", 10)
    )

    text.pack(pady=10)

    try:

        with open("bmi_data.json", "r") as file:
            data = json.load(file)

        if len(data) == 0:
            text.insert(tk.END, "No records found.")
            return

        for record in data:

            text.insert(
                tk.END,
                f"Name      : {record['name']}\n"
                f"Gender    : {record.get('gender', '-')}\n"
                f"Weight    : {record['weight']} kg\n"
                f"Height    : {record['height']} m\n"
                f"BMI       : {record['bmi']}\n"
                f"Category  : {record['category']}\n"
                f"Date      : {record['date']}\n"
                f"Time      : {record['time']}\n"
                + "-" * 60 + "\n"
            )
    except FileNotFoundError:

        text.insert(tk.END, "History file not found.")
def show_statistics():

    stats_window = tk.Toplevel(root)
    stats_window.title("BMI Statistics")
    stats_window.geometry("450x400")
    stats_window.configure(bg="#F8E8FF")

    title = tk.Label(
        stats_window,
        text="BMI Statistics",
        font=("Arial",18,"bold"),
        bg="#F8E8FF",
        fg="#7B2CBF"
    )

    title.pack(pady=15)

    try:

        with open("bmi_data.json","r") as file:
            data = json.load(file)

        if len(data) == 0:

            tk.Label(
                stats_window,
                text="No records available.",
                bg="#F8E8FF",
                font=("Arial",12)
            ).pack()

            return

        bmi_values = [record["bmi"] for record in data]

        total_users = len(data)
        average_bmi = round(sum(bmi_values)/total_users,2)
        highest_bmi = max(bmi_values)
        lowest_bmi = min(bmi_values)

        underweight = 0
        normal = 0
        overweight = 0
        obese = 0

        for record in data:

            if record["category"] == "Underweight":
                underweight +=1

            elif record["category"] == "Normal Weight":
                normal +=1

            elif record["category"] == "Overweight":
                overweight +=1

            else:
                obese +=1

        info = f"""
Total Users : {total_users}

Average BMI : {average_bmi}

Highest BMI : {highest_bmi}

Lowest BMI : {lowest_bmi}

Underweight : {underweight}

Normal : {normal}

Overweight : {overweight}

Obese : {obese}
"""

        tk.Label(
            stats_window,
            text=info,
            justify="left",
            bg="#F8E8FF",
            font=("Arial",12)
        ).pack()

    except FileNotFoundError:

        tk.Label(
            stats_window,
            text="History file not found.",
            bg="#F8E8FF"
        ).pack()


def show_graph():

    try:

        with open("bmi_data.json", "r") as file:
            data = json.load(file)

        if len(data) == 0:
            messagebox.showinfo(
                "No Data",
                "No records available to display."
            )
            return

        names = []
        bmi_values = []

        for record in data:
            names.append(record["name"])
            bmi_values.append(record["bmi"])

        plt.figure(figsize=(8,5))

        colors = []

        for value in bmi_values:

            if value < 18.5:
                colors.append("skyblue")

            elif value < 25:
                colors.append("green")

            elif value < 30:
                colors.append("orange")

            else:
                colors.append("red")

        plt.bar(names, bmi_values, color=colors)

        plt.title("BMI Trend Analysis of Users")
        plt.xlabel("Users")
        plt.ylabel("BMI")
        plt.axhline(18.5, color="skyblue", linestyle="--")
        plt.axhline(25, color="green", linestyle="--")
        plt.axhline(30, color="orange", linestyle="--")

        legend_elements = [
    Patch(facecolor="skyblue", label="Underweight"),
    Patch(facecolor="green", label="Normal Weight"),
    Patch(facecolor="orange", label="Overweight"),
    Patch(facecolor="red", label="Obese")
]

        plt.legend(handles=legend_elements)


        plt.tight_layout()
        plt.grid(axis="y", linestyle="--", alpha=0.5)

        plt.show()

    except FileNotFoundError:

        messagebox.showerror(
            "Error",
            "History file not found."
        )

def clear_fields():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    bmi_label.config(text="BMI :")
    category_label.config(
    text="Category :",
    fg="black"
)
    tip_label.config(text="Health Tip :")
    ideal_label.config(text="Ideal Weight :")
    score_label.config(text="Health Score :")
    gender_var.set("Male")

    name_entry.focus()
def save_data(name, gender, weight, height, bmi, category):

    filename = "bmi_data.json"

    record = {
        "name": name.title(),
        "gender": gender,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%I:%M %p")
    }

    if os.path.exists(filename):

        with open(filename, "r") as file:
            data = json.load(file)

    else:
        data = []

    data.append(record)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
# ---------------- Window ---------------- #

root = tk.Tk()
root.title("BMI Health Calculator")
root.geometry("550x700")
root.resizable(False, False)
root.configure(bg="#F8E8FF")

# ---------------- Heading ---------------- #

heading = tk.Label(
    root,
    text="BMI HEALTH CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="#F8E8FF",
    fg="#7B2CBF"
)
heading.pack(pady=20)

# ---------------- Name ---------------- #

name_label = tk.Label(
    root,
    text="Enter Name",
    font=("Arial", 12, "bold"),
    bg="#F8E8FF",
    fg="#3A86FF"
)
name_label.pack()

name_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 13),
    justify="center",
    bd=3
)
name_entry.pack(pady=8)

# ---------------- Gender ---------------- #

gender_label = tk.Label(
    root,
    text="Gender",
    font=("Arial", 12, "bold"),
    bg="#F8E8FF",
    fg="#3A86FF"
)

gender_label.pack()

gender_var = tk.StringVar(value="Male")

gender_frame = tk.Frame(root, bg="#F8E8FF")
gender_frame.pack(pady=5)

male_radio = tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    bg="#F8E8FF",
    font=("Arial",11)
)

male_radio.pack(side="left", padx=15)

female_radio = tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    bg="#F8E8FF",
    font=("Arial",11)
)

female_radio.pack(side="left", padx=15)

# ---------------- Weight ---------------- #

weight_label = tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 12, "bold"),
    bg="#F8E8FF",
    fg="#3A86FF"
)
weight_label.pack()

weight_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 13),
    justify="center",
    bd=3
)
weight_entry.pack(pady=8)

# ---------------- Height ---------------- #

height_label = tk.Label(
    root,
    text="Height (m)",
    font=("Arial", 12, "bold"),
    bg="#F8E8FF",
    fg="#3A86FF"
)
height_label.pack()

height_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 13),
    justify="center",
    bd=3
)
height_entry.pack(pady=8)

# ---------------- Buttons ---------------- #

button_frame = tk.Frame(root, bg="#F8E8FF")
button_frame.pack(pady=10)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate",
    command=calculate_bmi,
    width=14,
    bg="#FF66C4",
    fg="white",
    font=("Arial",11,"bold")
)
calculate_btn.grid(row=0, column=0, padx=8, pady=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=14,
    bg="#3A86FF",
    fg="white",
    font=("Arial",11,"bold")
)
clear_btn.grid(row=0, column=1, padx=8, pady=5)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    width=14,
    bg="#E63946",
    fg="white",
    font=("Arial",11,"bold")
)
exit_btn.grid(row=0, column=2, padx=8, pady=5)

history_btn = tk.Button(
    button_frame,
    text="History",
    command=view_history,
    width=14,
    bg="#00B894",
    fg="white",
    font=("Arial",11,"bold")
)
history_btn.grid(row=1, column=0, padx=8, pady=5)

stats_btn = tk.Button(
    button_frame,
    text="Statistics",
    command=show_statistics,
    width=14,
    bg="#FF9F1C",
    fg="white",
    font=("Arial",11,"bold")
)
stats_btn.grid(row=1, column=1, padx=8, pady=5)

graph_btn = tk.Button(
    button_frame,
    text="Graph",
    command=show_graph,
    width=14,
    bg="#6C5CE7",
    fg="white",
    font=("Arial",11,"bold")
)
graph_btn.grid(row=1, column=2, padx=8, pady=5)
# ---------------- Result Section ---------------- #

result_frame = tk.LabelFrame(
    root,
    text="Result",
    font=("Arial", 12, "bold"),
    bg="#F8E8FF",
    fg="#7B2CBF",
    padx=20,
    pady=15
)

result_frame.pack(padx=20, pady=10, fill="x")

bmi_label = tk.Label(
    result_frame,
    text="BMI :",
    font=("Arial", 12),
    bg="#F8E8FF"
)
bmi_label.pack(anchor="w", pady=5)

category_label = tk.Label(
    result_frame,
    text="Category :",
    font=("Arial", 12),
    bg="#F8E8FF"
)
category_label.pack(anchor="w", pady=5)

tip_label = tk.Label(
    result_frame,
    text="Health Tip :",
    font=("Arial", 12),
    bg="#F8E8FF"
)
tip_label.pack(anchor="w", pady=5)

ideal_label = tk.Label(
    result_frame,
    text="Ideal Weight :",
    font=("Arial", 12),
    bg="#F8E8FF"
)
ideal_label.pack(anchor="w", pady=5)
score_label = tk.Label(
    result_frame,
    text="Health Score :",
    font=("Arial", 12),
    bg="#F8E8FF"
)

score_label.pack(anchor="w", pady=5)

root.mainloop()
