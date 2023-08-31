from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("665x400+550+250")
        self.root.configure(bg="#B5E5CF")

        self.tasks = []

        self.the_connection = sql.connect('listOfTasks.db')
        self.the_cursor = self.the_connection.cursor()
        self.the_cursor.execute('create table if not exists tasks (title text)')

        self.create_widgets()

        self.retrieve_database()
        self.list_update()

    def create_widgets(self):
        self.functions_frame = Frame(self.root, bg="pink")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.task_label = Label(self.functions_frame, text="Enter the Task:",
                                font=("Times", "10", "bold"),
                                background="black", foreground="white")
        self.task_label.place(x=10, y=20)

        self.task_field = Entry(self.functions_frame,
                                font=("Times", "10"),
                                width=42,
                                foreground="black", background="white")
        self.task_field.place(x=160, y=30)

        self.add_button = Button(self.functions_frame,
                                 text="Add Task",
                                 width=10,
                                 bg='#D4AC0D', font=("Times", "10", "bold"),
                                 command=self.add_task)
        self.del_button = Button(self.functions_frame,
                                 text="Delete Task",
                                 width=10,
                                 bg='#D4AC0D', font=("Times", "10", "bold"),
                                 command=self.delete_task)
        self.del_all_button = Button(self.functions_frame,
                                     text="Delete All Tasks",
                                     width=12,
                                     font=("Times", "10", "bold"),
                                     bg='#D4AC0D',
                                     command=self.delete_all_tasks)
        self.exit_button = Button(self.functions_frame,
                                  text="Exit",
                                  width=44,
                                  bg='#D4AC0D', font=("Times", "10", "bold"),
                                  command=self.close)

        self.add_button.place(x=18, y=80)
        self.del_button.place(x=240, y=80)
        self.del_all_button.place(x=460, y=80)
        self.exit_button.place(x=17, y=330)

        self.task_listbox = Listbox(self.functions_frame,
                                    width=57,
                                    height=7,
                                    font="bold",
                                    selectmode='SINGLE',
                                    background="WHITE",
                                    foreground="BLACK",
                                    selectbackground="#D4AC0D",
                                    selectforeground="BLACK")
        self.task_listbox.place(x=17, y=140)

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.the_cursor.execute('insert into tasks values (?)', (task_string,))
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
                self.the_cursor.execute('delete from tasks where title = ?', (the_value,))
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while len(self.tasks) != 0:
                self.tasks.pop()
            self.the_cursor.execute('delete from tasks')
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        print(self.tasks)
        self.guiWindow.destroy()

    def retrieve_database(self):
        while len(self.tasks) != 0:
            self.tasks.pop()
        for row in self.the_cursor.execute('select title from tasks'):
            self.tasks.append(row[0])

if __name__ == "__main__":
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()