import tkinter as tk
from tkinter import messagebox
import json

class TodoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()

        
        self.title_entry = tk.Entry(root, width=50)
        self.description_entry = tk.Entry(root, width=50)
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        
        
        self.title_entry.grid(row=0, column=0, padx=10, pady=10)
        self.description_entry.grid(row=1, column=0, padx=10, pady=10)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        self.delete_button.grid(row=3, column=0, padx=10, pady=10)
        self.task_listbox.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

        self.display_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title and description:
            task = {"title": title, "description": description, "status": "Incomplete"}
            self.tasks.append(task)
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter both title and description.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.save_tasks()
            self.display_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['status']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoAppGUI(root)
    root.mainloop()
