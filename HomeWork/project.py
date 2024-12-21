import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Install with pip install tkcalendar

class Library:
    def __init__(self):  # Corrected from _init_ to __init__
        self.books = ["Python Basics", "Data Structures", "Artificial Intelligence", "Algorithms", "Java Programming"]

    def display_books(self):
        return "\n".join(self.books)

    def issue_book(self, book_name, issue_date):
        if book_name in self.books:
            self.books.remove(book_name)
            return f"'{book_name}' issued successfully on {issue_date}."
        return f"'{book_name}' is not available or already issued."

    def return_book(self, book_name, return_date):
        self.books.append(book_name)
        return f"'{book_name}' returned successfully on {return_date}."

    def add_book(self, book_name):
        self.books.append(book_name)
        return f"'{book_name}' added to the library."

class LibraryGUI:
    def __init__(self, root, library): 
        self.library = library
        self.root = root
        self.root.geometry("450x500")

        # Heading
        heading = tk.Label(root, text="Library Management System", font=("Arial", 16), pady=10)
        heading.pack()

        # Display Books Button
        self.display_button = tk.Button(root, text="Display Books", width=20, command=self.display_books)
        self.display_button.pack(pady=5)

        # Issue Book
        self.issue_label = tk.Label(root, text="Issue Book:")
        self.issue_label.pack(pady=5)
        self.issue_entry = tk.Entry(root, width=30)
        self.issue_entry.pack()
        self.issue_date_label = tk.Label(root, text="Select Issue Date:")
        self.issue_date_label.pack(pady=5)
        self.issue_date = DateEntry(root, width=27, background='darkblue', foreground='white', borderwidth=2)
        self.issue_date.pack(pady=5)
        self.issue_button = tk.Button(root, text="Issue", command=self.issue_book)
        self.issue_button.pack(pady=5)

        # Return Book
        self.return_label = tk.Label(root, text="Return Book:")
        self.return_label.pack(pady=5)
        self.return_entry = tk.Entry(root, width=30)
        self.return_entry.pack()
        self.return_date_label = tk.Label(root, text="Select Return Date:")
        self.return_date_label.pack(pady=5)
        self.return_date = DateEntry(root, width=27, background='darkblue', foreground='white', borderwidth=2)
        self.return_date.pack(pady=5)
        self.return_button = tk.Button(root, text="Return", command=self.return_book)
        self.return_button.pack(pady=5)

        # Add Book
        tk.Label(root, text="Add New Book:").pack(pady=5)
        self.add_entry = tk.Entry(root, width=30)
        self.add_entry.pack()
        tk.Button(root, text="Add", command=self.add_book).pack(pady=5)

    def display_books(self):
        books = self.library.display_books()
        messagebox.showinfo("Available Books", f"Books in the Library:\n{books}")

    def issue_book(self):
        book_name = self.issue_entry.get().strip()
        issue_date = self.issue_date.get()
        if not book_name:
            messagebox.showerror("Error", "Please enter a book name.")
            return
        message = self.library.issue_book(book_name, issue_date)
        messagebox.showinfo("Issue Book", message)
        self.issue_entry.delete(0, tk.END)

    def return_book(self):
        book_name = self.return_entry.get().strip()
        return_date = self.return_date.get()
        if not book_name:
            messagebox.showerror("Error", "Please enter a book name.")
            return
        message = self.library.return_book(book_name, return_date)
        
        messagebox.showinfo("Return Book", message)
        self.return_entry.delete(0, tk.END)

    def add_book(self):
        book_name = self.add_entry.get().strip()
        if not book_name:
            messagebox.showerror("Error", "Please enter a book name.")
            return
        message = self.library.add_book(book_name)
        messagebox.showinfo("Add Book", message)
        self.add_entry.delete(0, tk.END)

if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    gui = LibraryGUI(root, library)
    root.mainloop()