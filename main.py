 import datetime

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.author = ""  # New feature: Author
        self.genre = ""   # New feature: Genre
        self.status = "Available"
        self.lender_name = ""
        self.lend_date = ""
        self.return_date = None  # New feature: Return date

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_books(self, titles):
        for i, title in enumerate(titles, start=1000):
            self.books[str(i)] = Book(str(i), title)

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title", "\t\t\t", "Status")
        print("----------------------------------------------------------")
        for book_id, book in self.books.items():
            print(book_id, "\t\t", book.title)
            print("\t\t\t", book.status)
            print("----------------------------------------------------------")

    def search_books(self, keyword):
        found_books = []
        for book_id, book in self.books.items():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def issue_book(self, book_id, lender_name):
        book = self.books.get(book_id)
        if book:
            if book.status == "Available":
                book.status = "Issued"
                book.lender_name = lender_name
                book.lend_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # New feature: Set return date (7 days from issue date)
                book.return_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
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
                book.return_date = None  # Clear return date
                print("Book returned successfully!")
            else:
                print("This book is not issued.")
        else:
            print("Book not found.")

    def display_book_details(self, book_id):
        book = self.books.get(book_id)
        if book:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Genre:", book.genre)
            print("Status:", book.status)
            print("Lender Name:", book.lender_name)
            print("Issue Date:", book.lend_date)
            print("Return Date:", book.return_date)
        else:
            print("Book not found.")

if __name__ == "__main__":
    library = Library("Python's Library")

    # List of book titles
    book_titles = [
        "Introduction to Computer Science",
        "Algorithms and Data Structures",
        # Add more book titles here...
    ]

    # Add books to the library
    library.add_books(book_titles)

    while True:
        print("\n----------Welcome To", library.name, "---------")
        print("1. Display Books")
        print("2. Search Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Book Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            keyword = input("Enter a keyword to search: ")
            found_books = library.search_books(keyword)
            if found_books:
                print("Found Books:")
                for book in found_books:
                    print(book.title)
            else:
                print("No books found.")
        elif choice == "3":
            book_id = input("Enter the book ID to issue: ")
            lender_name = input("Enter your name: ")
            library.issue_book(book_id, lender_name)
        elif choice == "4":
            book_id = input("Enter the book ID to return: ")
            library.return_book(book_id)
        elif choice == "5":
            book_id = input("Enter the book ID to display details: ")
            library.display_book_details(book_id)
        elif choice == "6":
            print("Thank you for using the library. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


