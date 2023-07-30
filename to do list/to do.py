import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, text):
        self.text = text
        self.editing = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        
        header_frame = tk.Frame(root, bg="green", height=50)
        header_frame.pack_propagate(0)  
        header_frame.pack(side=tk.TOP, fill=tk.X)

        header_label = tk.Label(header_frame, text="ToDo List", font=("Helvetica", 20, "bold"), fg="black", bg="green")
        header_label.pack(pady=10, padx=10, anchor=tk.W)

        
        tasks_frame = tk.Frame(root, bg="white")
        tasks_frame.pack(fill=tk.BOTH, expand=True)

        
        add_item_label = tk.Label(tasks_frame, text="Add Items", font=("Helvetica", 16, "bold"), bg="white")
        add_item_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.task_entry = tk.Entry(tasks_frame, font=("Helvetica", 14), relief=tk.FLAT, bd=2, highlightbackground="lightgrey", highlightcolor="black")
        self.task_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

        self.task_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.task_entry.bind("<FocusOut>", self.on_entry_focus_out)

        submit_button = tk.Button(tasks_frame, text="Submit", command=self.add_task, fg="white", bg="black")
        submit_button.grid(row=1, column=2, padx=10, pady=5)

        
        tasks_label = tk.Label(tasks_frame, text="Tasks", font=("Helvetica", 16, "bold"), bg="white")
        tasks_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)

        self.task_list_frame = tk.Frame(tasks_frame, bg="white")
        self.task_list_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        self.tasks = []

    def on_entry_focus_in(self,event):
        self.task_entry.config(fg="black", relief=tk.SOLID, bd=2, highlightbackground="lightblue", highlightcolor="lightblue")

    def on_entry_focus_out(self,event):
        self.task_entry.config(fg="gray", relief=tk.FLAT, highlightbackground="lightgrey", highlightcolor="black")

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            task = Task(task_text)
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

            
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")
    def edit_task(self, task):
        if task.editing:
            task.text = task.edit_entry.get()
            task.edit_entry.destroy()
            task.label.config(text=task.text)
            task.edit_button.config(text="Edit")
            task.editing = False

            
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, task.text)
        else:
            task.editing = True
            task.edit_entry = tk.Entry(task.frame, width=30)
            task.edit_entry.insert(tk.END, task.text)
            task.edit_entry.pack(side=tk.LEFT)
            task.edit_entry.focus_set()
            task.label.config(text="")


    
    def delete_task(self, task):
        self.tasks.remove(task)
        self.update_task_list()

    def update_task_list(self):
        
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        
        for task in self.tasks:
            task.frame = tk.Frame(self.task_list_frame, bg="white", relief=tk.RAISED, bd=1)
            task.frame.pack(pady=5, padx=5, fill=tk.X, expand=True)

            task.label = tk.Label(task.frame, text=task.text, bg="white")
            task.label.pack(side=tk.LEFT, anchor=tk.W)

            
            delete_button = tk.Button(task.frame, text="Delete", command=lambda t=task: self.delete_task(t),fg="white", bg="red")
            delete_button.pack(side=tk.RIGHT)


            edit_button = tk.Button(task.frame, text="Edit", command=lambda t=task: self.edit_task(t),fg="white", bg="green")
            edit_button.pack(side=tk.RIGHT)


root = tk.Tk()
todo_app = ToDoListApp(root)

root.mainloop()