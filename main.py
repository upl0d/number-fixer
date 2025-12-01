import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
root = tk.Tk()

def browser_file():
    
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    selected_file_entry.delete(0,tk.END)
    selected_file_entry.insert(0,file)
    return file

def excute_btn():
    info_text.delete(1.0, tk.END)

    prefixes = ("00966","5","05")
    line_modified = []
    file = selected_file_entry.get()
    new_file = new_file_entry.get()
    folder_path = os.path.dirname(file)
    new_path = os.path.join(folder_path, new_file)
    if not new_file.endswith(".txt"):
        new_file += ".txt"
        new_file_entry.delete(0, tk.END)
        new_file_entry.insert(0, new_file)
    if not new_file:
        messagebox.showerror("خطأ", "اسم الملف فارغ!")
        return

    if not file:
       messagebox.showerror("خطأ", "المسار فارغ!")
       return
    with open(file, "r") as f:
        lines = f.readlines()
        if not lines:
            messagebox.showerror("خطأ", "الملف فارغ!")
            return
        for line in lines:
            for prefix in prefixes:
                if line.startswith(prefix):
                    number_only = line.strip()[len(prefix):]
                    if len(number_only) == 9:
                        line = line.replace(prefix,"966", 1)
                    
                        break
            line_modified.append(line)
    with open(new_path, "w") as f:
        for line in line_modified:
            f.write(line)
    info_text.insert(tk.END, f"عدد السطور المعالجة: {len(line_modified)}\n")

root.geometry("300x300")

#-----[Disable window resizeable]
root.resizable(False,False)
#-----[btn]-----#
btn = tk.Button(root, text="استعراض", command=browser_file)
btn.place(x=10, y=10, width=80,height=25)
#-----[Entry browse file name]-----#
selected_file_entry = tk.Entry(root)
selected_file_entry.place(x=100, y=10, width=190, height=25)
#-----[Entry New file name]-----#
new_file_entry = tk.Entry(root)
new_file_entry.place(x=10, y=50, width=190, height=25)
#-----[Excute btn]-----#
excute_btn = tk.Button(root, text="تنفيذ", command=excute_btn)
excute_btn.place(x=210, y=50, width=80, height=25)
#-----[process]-----#
info_text = tk.Text(root)
info_text.place(x=10, y=130, width=280, height=160)
#-----[Logic]-----#

    
root.mainloop()