""" 
Antonio Leon
09/11/2023
Last Updated: 10/22/2023
To-Do List
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
import subprocess

class TodoApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("700x500")
        self.window.title("To-Do List")
        self.window.configure(bg="#f5eeed")
        self.window.resizable(False, False)
        icon = PhotoImage(file="C:\\Users\\jose-\\OneDrive\\Documents\\Python Programs\\ToDoList\\icon.png")
        self.window.iconphoto(True, icon)

        self.reminders_list = []
        self.trash_list = []
        self.completed_count = []

        self.create_gui()

    def create_gui(self):
        #1st Canvas.
        self.canvas_1 = tk.Canvas(window, width=680, height=35, bg="#4a4a4a", highlightthickness=1, highlightbackground="black")
        self.canvas_1.pack(padx=5, pady=5)

        #Canvas.
        self.mainCanvas = tk.Canvas(window, width=680, height=480, bg="white", highlightthickness=1, highlightbackground="black")
        self.mainCanvas.pack(padx=5, pady=5)

        self.toolsCanvas = tk.Canvas(window, width=130, height=345, bg="#4a4a4a", highlightthickness=1, highlightbackground="black")
        self.mainCanvas.create_window(76, 213, window=self.toolsCanvas)
        
        #Buttons.
        self.reset_button = tk.Button(window, text="Reset", relief=FLAT, bg="gray", width=10, height=1, command=self.reset)
        self.canvas_1.create_window(75, 19, window=self.reset_button)

        self.save_button = tk.Button(window, text="Save", relief=FLAT, bg="gray", command=self.save_both_remtrs, width=10, height=1)
        self.canvas_1.create_window(195, 19, window=self.save_button)
        
        self.all_reminders_button = tk.Button(window, text="All Reminders", bg="gray", width=15, height=2, command=self.display_reminders)
        self.toolsCanvas.create_window(66, 60, window=self.all_reminders_button)

        self.trash_button = tk.Button(window, text="Trash", bg="gray", width=15, height=2, command=self.display_trash)
        self.toolsCanvas.create_window(66, 120, window=self.trash_button)
        
        #Create a context menu.
        self.context_menu = tk.Menu(self.window, tearoff=0)
        self.context_menu.add_command(label="Completed", command=self.completed_reminder)
        self.context_menu.add_command(label="Trash", command=self.delete_reminder)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Version 1.0.4", command="")
        
        #Label that shows how many task have been completed.
           
    def limit_input(self, P):
        if len(P) <= 65: 
            return True
        else:
            return False
    
    def show_menu(self, event):
        seleted_item = self.listBox.curselection()
        if seleted_item:
            index = seleted_item[0]
            self.context_menu.post(event.x_root, event.y_root)
            
    def reset(self):
        self.window.destroy()
        subprocess.Popen([sys.executable] + sys.argv)

    def display_reminders(self):
        self.listBoxCanvas = tk.Canvas(window, width=522, height=395, bg="white", highlightthickness=0, highlightbackground="black")
        self.mainCanvas.create_window(411, 237, window=self.listBoxCanvas)
        
        self.listBox = tk.Listbox(window, selectmode=tk.SINGLE, width=47, height=15, font="Helvetica 14", bg="#4a4a4a", fg="white", relief="flat", yscrollcommand=TRUE)
        self.listBoxCanvas.create_window(261, 173, window=self.listBox)
        self.listBox.bind("<Button-3>", self.show_menu)
        
        self.reminders_label = tk.Label(window, text="Reminders", font=("times new roman", 18), bg="white")
        self.mainCanvas.create_window(405, 20, window=self.reminders_label)
        
        #Entry Box to add new task/reminder.
        self.validation = window.register(self.limit_input)
        self.add_task_entry = tk.Entry(window, width=37, highlightthickness=1, highlightbackground="black", validate="key", validatecommand=(self.validation, "%P"))
        self.listBoxCanvas.create_window(261, 375, window=self.add_task_entry)
        self.add_task_entry.config(font=("Arial", 13))
        self.add_task_entry.bind("<Return>", self.add_new_reminder)
        
        #Buttons flag blue and green.
        self.flag_blue_button = tk.Button(window, text="Flag Blue", bg="gray", width=10, height=1, command=self.flag_blue_function)
        self.listBoxCanvas.create_window(41, 375, window=self.flag_blue_button)
        
        self.flag_green_button = tk.Button(window, text="Flag Green", bg="gray", width=10, height=1, command=self.flag_green_function)
        self.listBoxCanvas.create_window(481, 375, window=self.flag_green_button)
        
        for ii in [self.reminders_list]:
            for i in ii:
                self.listBox.insert(tk.END, i[0])
                if i[1] == "TRUE":
                    self.listBox.itemconfig(tk.END, {"bg": "red"})
                elif i[2] == "TRUE":
                    self.listBox.itemconfig(tk.END, {"bg": "blue"})
                elif i[3] == "TRUE":
                    self.listBox.itemconfig(tk.END, {"bg": "green"})
             
    def display_trash(self):
        #Trash Canvas.
        self.listBoxTrashCanvas = tk.Canvas(window, width=522, height=395, bg="white", highlightthickness=0, highlightbackground="black")
        self.mainCanvas.create_window(411, 237, window=self.listBoxTrashCanvas)

        #List Box Trash.
        self.listBoxTrash = tk.Listbox(window, selectmode=tk.SINGLE, width=47, height=15, font="Helvetica 14", bg="#4a4a4a", fg="white", relief="flat", yscrollcommand=TRUE)
        self.listBoxTrashCanvas.create_window(261, 173, window=self.listBoxTrash)
        
        #Label.
        self.trash_label = tk.Label(window, text="Trash", font=("times new roman", 18), bg="white", width=10)
        self.mainCanvas.create_window(405, 20, window=self.trash_label)
        
        #Buttons to delete items.
        self.delete_allTrash_button = tk.Button(window, text="Delete All", bg="gray", width=35, height=1, command=self.delete_all_trash)
        self.listBoxTrashCanvas.create_window(129, 375, window=self.delete_allTrash_button)
        
        self.delete_trash_button = tk.Button(window, text="Delete", bg="gray", width=35, height=1, command=self.delete_trash)
        self.listBoxTrashCanvas.create_window(393, 375, window=self.delete_trash_button)
        
        #Logic to display items.
        for ii in [self.trash_list]:
            for i in ii:
                self.listBoxTrash.insert(tk.END, i[0])
                if i[1] == "TRUE":
                    self.listBoxTrash.itemconfig(tk.END, {"bg": "red"})
    
    def delete_all_trash(self):
        self.trash_list.clear()
        self.listBoxTrash.delete(0, tk.END)
    
    def delete_trash(self):
        seleted_item = self.listBoxTrash.curselection()
        if seleted_item:
            index = seleted_item[0]
            text_to_remove = self.listBoxTrash.get(index)
            
            for ii in [self.trash_list]:
                for i in ii:
                    if i[0] == text_to_remove:
                        self.trash_list.remove(i)
            
            self.listBoxTrash.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task/reminder to delete.")
             
    def add_new_reminder(self, event):
        new_reminder = self.add_task_entry.get()
        completed = "FALSE"
        flag_blue = "FALSE"
        flag_green = "FALSE"
        
        if new_reminder:
            self.reminders_list.append([new_reminder, completed, flag_blue, flag_green])
            self.listBox.insert(tk.END, new_reminder)
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def completed_reminder(self):
        seleted_item = self.listBox.curselection()
        if seleted_item:
            index = seleted_item[0]
            self.listBox.itemconfig(index, {"bg": "red"})
            text_to_remove = self.listBox.get(index)
            
            for items in [self.reminders_list]:
                for item in items:
                    if item[0] == text_to_remove:
                        item[1] = "TRUE"
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_reminder(self):
        selected_item = self.listBox.curselection()
        if selected_item:
            index = selected_item[0]
            text_to_remove = self.listBox.get(index)
            
            for items in [self.reminders_list]:
                for item in items:
                    if item[0] == text_to_remove:
                        self.trash_list.append([item[0], item[1]])
                        self.reminders_list.remove(item)
            
            self.listBox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def flag_blue_function(self):
        selected_item = self.listBox.curselection()
        if selected_item:
            index = selected_item[0]
            self.listBox.itemconfig(index, {"bg": "blue"})
            text = self.listBox.get(index)
            
            for items in [self.reminders_list]:
                for item in items:
                    if item[0] == text:
                        item[2] = "TRUE"
        else:
            messagebox.showwarning("Warning", "Please select a task.")
            
    def flag_green_function(self):
        selected_item = self.listBox.curselection()
        if selected_item:
            index = selected_item[0]
            self.listBox.itemconfig(index, {"bg": "green"})
            text = self.listBox.get(index)
            
            for items in [self.reminders_list]:
                for item in items:
                    if item[0] == text:
                        item[3] = "TRUE"
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def load_trash_list(self):
        try:
            with open("trash_list.txt", "r", encoding="utf8") as _f:
                for line in _f:
                    item0, item1, item2, item3 = line.strip().split(", ")
                    self.trash_list.append([item0, item1, item2, item3])
        
        except FileNotFoundError:
            return []
            
    def load_reminders_list(self):
        try:
            with open("remindersList.txt", "r", encoding="utf8") as _f:
                for line in _f:
                    item0, item1, item2, item3 = line.strip().split(", ")
                    self.reminders_list.append([item0, item1, item2, item3])
                    
        except FileNotFoundError:
            return []  

    def save_trash_list(self):
        with open("trash_list.txt", "w", encoding="utf8") as _f:
            for items in [self.trash_list]:
                for item in items:
                    _f.write(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}\n")

    def save_reminders_list(self):
        with open("remindersList.txt", "w", encoding="utf8") as _f:
            for items in [self.reminders_list]:
                for item in items:
                    _f.write(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}\n")
                
        messagebox.showinfo("Info", "Saved!")

    def save_both_remtrs(self):
        self.save_reminders_list()
        self.save_trash_list()
    
    def run(self):
        self.load_reminders_list()
        self.load_trash_list()
        self.display_reminders()
        self.window.mainloop()

if __name__ == "__main__":
    window = Tk()
    todo_app = TodoApp(window)
    todo_app.run()