import tkinter as tk
from tkinter import messagebox
import json
import uuid

class Task:
    def __init__(self, title, description):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = "Incomplete"

    def __repr__(self):
        return f"{self.title} - {self.status}"

class TodoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()

        
        self.title_label = tk.Label(root, text="Title:")
        self.title_entry = tk.Entry(root, width=50)
        self.description_label = tk.Label(root, text="Description:")
        self.description_entry = tk.Entry(root, width=50)
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)

       
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)
        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.display_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
                return [Task(task["title"], task["description"]) for task in tasks]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        tasks = [{"id": task.id, "title": task.title, "description": task.description, "status": task.status} for task in self.tasks]
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title and description:
            task = Task(title, description)
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
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoAppGUI(root)
    root.mainloop()

