import datetime

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.status = "Available"
        self.lender_name = ""
        self.lend_date = ""

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = Book(book_id, title)

    def display_books(self):
        print("Book ID\t\tTitle\t\t\t\tStatus")
        for book_id, book in self.books.items():
            print(f"{book_id}\t\t{book.title}\t\t{book.status}")

    def issue_book(self, book_id, lender_name):
        book = self.books.get(book_id)
        if book:
            if book.status == "Available":
                book.status = "Issued"
                book.lender_name = lender_name
                book.lend_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Book issued successfully!")
            else:
                print("Sorry, the book is not available.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if book:
            if book.status == "Issued":
                book.status = "Available"
                book.lender_name = ""
                book.lend_date = ""
                print("Book returned successfully!")
            else:
                print("This book is not issued.")
        else:
            print("Book not found.")

if __name__ == "__main__":
    library = Library("Python's Library")

    book_titles = [
        "Introduction to Computer Science",
        "Algorithms and Data Structures",
        # Add more book titles here if needed
    ]

    for i, title in enumerate(book_titles, start=1000):
        library.add_book(str(i), title)

    while True:
        print("\n----------Welcome To", library.name, "---------")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book_id = input("Enter the book ID: ")
            lender_name = input("Enter your name: ")
            library.issue_book(book_id, lender_name)
        elif choice == "3":
            book_id = input("Enter the book ID: ")
            library.return_book(book_id)
        elif choice == "4":
            print("Thank you for using the library. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
