import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
from update_checker import checkUpdate
import threading
import time

root = tk.Tk()

# تحديد مسار البرنامج سواء EXE أو تشغيل عادي
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# قراءة الإصدار من version.txt
def read_version():
    version_file_path = os.path.join(BASE_PATH, "version.txt")
    with open(version_file_path, "r", encoding="utf-8") as f:
        return f.read().split('"')[1]
def print_info(msg):
    info_text.insert(tk.END,msg + "\n")
    info_text.see(tk.END)

def start_update_thread():
    threading.Thread(target=lambda: checkUpdate(version_label, print_info)).start()

def browser_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    selected_file_entry.delete(0,tk.END)
    selected_file_entry.insert(0,file)
    return file

def excute():
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

    with open(file, "r", encoding="utf-8") as f:
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

    with open(new_path, "w", encoding="utf-8") as f:
        for line in line_modified:
            f.write(line)
    info_text.insert(tk.END, f"عدد السطور المعالجة: {len(line_modified)}\n")

def current_version_display():
    return read_version()

root.geometry("300x300")
root.resizable(False,False)
root.title("PFixer")
icon_path = os.path.join(BASE_PATH, "favicon.ico")
root.iconbitmap(icon_path)
#-----[الأزرار والواجهه]-----
btn = tk.Button(root, text="استعراض", command=browser_file)
btn.place(x=10, y=10, width=80,height=25)

selected_file_entry = tk.Entry(root)
selected_file_entry.place(x=100, y=10, width=190, height=25)

new_file_entry = tk.Entry(root)
new_file_entry.place(x=10, y=50, width=190, height=25)

excute_btn = tk.Button(root, text="تنفيذ", command=excute)
excute_btn.place(x=210, y=50, width=80, height=25)

info_text = tk.Text(root)
info_text.place(x=10, y=130, width=280, height=130)

update_btn = tk.Button(root,text="تحديث", command=start_update_thread)
update_btn.place(x=150, y=265, width=80, height=25)

version_label = tk.Label(root, text=f"Current Version: [{current_version_display()}]")
version_label.place(x=5, y=265, width=150, height=25)

root.mainloop()
