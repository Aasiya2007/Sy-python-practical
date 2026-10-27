
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")
FIELDS = ["Name", "Roll No", "Class", "Div", "Course", "Marks"]

root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x700")
root.minsize(900, 600)
root.configure(bg="#EEF4FF")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=32, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"),
                background="#24558A", foreground="white")
style.map("Treeview", background=[("selected", "#A9D5FF")])

students = []
entries = {}


def save_data():
    try:
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for s in students:
                writer.writerow([s[x] for x in FIELDS])
        return True
    except OSError:
        messagebox.showerror("Error", "Unable to save records!")
        return False


def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", newline="", encoding="utf-8") as f:
                for row in csv.reader(f):
                    if len(row) == len(FIELDS):
                        students.append(dict(zip(FIELDS, row)))
        except (OSError, csv.Error):
            messagebox.showerror("Error", "Unable to read file!")
    show_records()


def show_records(records=None):
    table.delete(*table.get_children())
    data = students if records is None else records
    for i, s in enumerate(data, 1):
        table.insert("", "end", values=[i] + [s[x] for x in FIELDS])
    count_label.config(text=f"Total Records: {len(students)}")


def clear_fields():
    for e in entries.values():
        e.delete(0, tk.END)
    table.selection_remove(table.selection())


def get_data():
    data = {x: entries[x].get().strip() for x in FIELDS}
    if not all(data.values()):
        messagebox.showwarning("Warning", "Please fill all fields!")
        return None
    try:
        marks = float(data["Marks"])
        if not 0 <= marks <= 100:
            raise ValueError
        data["Marks"] = str(marks)
    except ValueError:
        messagebox.showerror("Invalid Marks", "Enter marks from 0 to 100!")
        return None
    return data


def add_student():
    data = get_data()
    if data is None:
        return
    if any(s["Roll No"] == data["Roll No"] for s in students):
        messagebox.showerror("Error", "Roll No already exists!")
        return
    students.append(data)
    if save_data():
        show_records()
        clear_fields()
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        students.pop()


def search_student():
    roll = entries["Roll No"].get().strip()
    if not roll:
        messagebox.showwarning("Search", "Enter Roll No in the form!")
        return
    found = [s for s in students if s["Roll No"] == roll]
    show_records(found)
    if found:
        table.selection_set(table.get_children()[0])
        messagebox.showinfo("Found", "Student record found!")
    else:
        messagebox.showinfo("Not Found", "Student not found!")


def update_student():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Update", "Select a student from the table!")
        return
    data = get_data()
    if data is None:
        return

    values = table.item(selected[0], "values")
    old_roll = str(values[2])
    if any(s["Roll No"] == data["Roll No"] and
           s["Roll No"] != old_roll for s in students):
        messagebox.showerror("Error", "Roll No already exists!")
        return

    index = next((i for i, s in enumerate(students)
                  if s["Roll No"] == old_roll), None)
    if index is None:
        return

    old_record = students[index].copy()
    students[index] = data
    if save_data():
        show_records()
        clear_fields()
        messagebox.showinfo("Success", "Student updated successfully!")
    else:
        students[index] = old_record
        show_records()


def delete_student():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Delete", "Select a student from the table!")
        return

    values = table.item(selected[0], "values")
    roll = str(values[2])

    if messagebox.askyesno("Confirm Delete", f"Delete Roll No {roll}?"):
        index = next((i for i, s in enumerate(students)
                      if s["Roll No"] == roll), None)
        if index is not None:
            removed = students.pop(index)
            if save_data():
                show_records()
                clear_fields()
                messagebox.showinfo("Success", "Student deleted!")
            else:
                students.insert(index, removed)
                show_records()


def select_record(event=None):
    selected = table.selection()
    if selected:
        values = table.item(selected[0], "values")[1:]
        for field, value in zip(FIELDS, values):
            entries[field].delete(0, tk.END)
            entries[field].insert(0, value)


def filter_records(*args):
    q = filter_var.get().strip().lower()
    found = [s for s in students if
             q in s["Name"].lower() or q in s["Roll No"].lower()]
    show_records(found)


# Header
header = tk.Frame(root, bg="#17365D", pady=18)
header.pack(fill="x")

tk.Label(header, text="🎓  STUDENT MANAGEMENT SYSTEM",
         font=("Arial", 22, "bold"), bg="#17365D",
         fg="white").pack()
tk.Label(header, text="Manage Students  •  Track Records  •  Build Your Future",
         font=("Arial", 10), bg="#17365D", fg="#D8E8FF").pack(pady=5)

main = tk.Frame(root, bg="#EEF4FF")
main.pack(fill="both", expand=True, padx=20, pady=15)

# Student Details
form = tk.LabelFrame(main, text="  Student Details  ",
                     font=("Arial", 12, "bold"), bg="white",
                     fg="#17365D", padx=15, pady=12)
form.pack(fill="x", pady=(0, 12))

for i, field in enumerate(FIELDS):
    row, col = divmod(i, 3)
    tk.Label(form, text=field + ":", bg="white",
             font=("Arial", 10, "bold")).grid(
        row=row, column=col * 2, sticky="w", padx=8, pady=12)

    e = tk.Entry(form, font=("Arial", 11), relief="solid", bd=1, width=23)
    e.grid(row=row, column=col * 2 + 1,
           sticky="ew", padx=7, pady=12, ipady=6)
    entries[field] = e
    form.columnconfigure(col * 2 + 1, weight=1)

# Centered Buttons
actions = tk.Frame(main, bg="#EEF4FF")
actions.pack(fill="x", pady=8)

button_frame = tk.Frame(actions, bg="#EEF4FF")
button_frame.pack(anchor="center")

for label, command, color in [
    ("＋ Add Student", add_student, "#0F9D76"),
    ("⌕ Search", search_student, "#7048D8"),
    ("✎ Update", update_student, "#2475E8"),
    ("✖ Delete", delete_student, "#E53950"),
    ("Clear", clear_fields, "#60758B")
]:
    tk.Button(button_frame, text=label, command=command,
              bg=color, fg="white", activebackground=color,
              activeforeground="white", font=("Arial", 10, "bold"),
              relief="flat", cursor="hand2", width=13, pady=9
              ).pack(side="left", padx=6)

# Student Records
records_box = tk.LabelFrame(main, text="  Student Records  ",
                            font=("Arial", 12, "bold"), bg="white",
                            fg="#17365D", padx=10, pady=10)
records_box.pack(fill="both", expand=True, pady=(12, 0))

toolbar = tk.Frame(records_box, bg="white")
toolbar.pack(fill="x", pady=(0, 10))

filter_var = tk.StringVar()
filter_var.trace_add("write", filter_records)

tk.Label(toolbar, text="Search by Name or Roll No:",
         bg="white", font=("Arial", 10)).pack(side="left")
tk.Entry(toolbar, textvariable=filter_var, font=("Arial", 10),
         width=25, relief="solid", bd=1).pack(
    side="left", padx=8, ipady=4)

count_label = tk.Label(toolbar, text="Total Records: 0",
                       bg="white", fg="#17365D",
                       font=("Arial", 10, "bold"))
count_label.pack(side="right")

frame = tk.Frame(records_box, bg="white")
frame.pack(fill="both", expand=True)

columns = ["#", *FIELDS]
table = ttk.Treeview(frame, columns=columns, show="headings",
                     selectmode="browse")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=110, anchor="center")

table.column("#", width=40)
table.column("Name", width=150)
table.column("Course", width=120)

scroll = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scroll.set)
table.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")
table.bind("<<TreeviewSelect>>", select_record)

tk.Label(root, text="Student Management System  |  Developed with Python",
         bg="#17365D", fg="white", font=("Arial", 9),
         pady=9).pack(fill="x")

load_data()
root.mainloop()
