import os
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

title_filename = "Filename"
prompt_filename = "Enter the full name of the file (e.g. myfile.txt):"


def create_file():
    path = filedialog.askdirectory(title="Select Directory")
    if not path:
        messagebox.showerror("Error", "Invalid or empty path!")
        return

    filename_with_extension = simpledialog.askstring(title_filename, 
                                                     prompt_filename)
    if not filename_with_extension:
        messagebox.showerror("Error", "Filename cannot be empty!")
        return

    full_path = os.path.join(path, filename_with_extension)
    if os.path.exists(full_path):
        messagebox.showerror("Error", "File already exists!")
        return

    with open(full_path, "w") as f:
        f.write("")

    messagebox.showinfo("Success", f"File created successfully at {full_path}")
    os.startfile(full_path)  # Open the file immediately after creating it


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    create_file()
