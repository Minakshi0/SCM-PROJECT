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

    def issue_book(self, book_id, lender_name):
        if book_id in self.books:
            book = self.books[book_id]
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
        if book_id in self.books:
            book = self.books[book_id]
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

    # List of book titles
    book_titles = [
        "Introduction to Computer Science",
        "Algorithms and Data Structures",
        "Computer Architecture: A Quantitative Approach",
        "Operating Systems Concepts",
        "Introduction to Programming with Python",
        "Artificial Intelligence: A Modern Approach",
        "Computer Networking: A Top-Down Approach",
        "Database Management Systems",
        "Introduction to Software Engineering",
        "Discrete Mathematics for Computer Science",
        "Principles of Computer Graphics",
        "Computer Organization and Design",
        "Introduction to Computer Security",
        "Introduction to Machine Learning",
        "Introduction to Computer Vision",
        "Computer Ethics and Professional Responsibility",
        "Programming Language Pragmatics",
        "Compilers: Principles, Techniques, and Tools",
        "Computer Networks: A Systems Approach",
        "Introduction to Parallel Computing",
        "Cryptography and Network Security",
        "Introduction to Human-Computer Interaction",
        "Software Testing and Analysis",
        "Web Development and Design",
        "Introduction to Embedded Systems",
        "Introduction to Cryptography",
        "Information Retrieval: Algorithms and Heuristics",
        "Computer Systems: A Programmer's Perspective",
        "Cloud Computing: Principles and Paradigms",
        "Computer Arithmetic: Algorithms and Hardware Designs",
        "Introduction to Data Science",
        "Principles of Digital Communication",
        "Mobile Computing: Technology and Applications",
        "Introduction to Cybersecurity",
        "Introduction to Quantum Computing",
        "Computer Vision: Algorithms and Applications",
        "Introduction to Computer Graphics Programming",
        "Distributed Systems: Concepts and Design",
        "Introduction to Formal Languages and Automata Theory",
        "Principles of Compiler Design",
        "Introduction to Computer Animation",
        "Real-Time Systems: Design and Analysis",
        "Computer Algebra: Systems and Algorithms",
        "Introduction to Information Theory",
        "Human-Robot Interaction: An Introduction",
        "Introduction to Natural Language Processing",
        "Digital Image Processing: Principles and Applications",
        "Introduction to Computational Biology",
        "Advanced Computer Architecture",
        "Introduction to Digital Signal Processing",
        "Machine Learning for Computer Vision",
        "Game Development: Principles and Practices",
        "Introduction to Computer Music",
        "Computer and Network Security: Principles and Practices",
        "Introduction to Pattern Recognition",
        "Introduction to Big Data Analytics",
        "Embedded Systems Design: Concepts and Practices",
        "Introduction to Computer Forensics",
        "Introduction to Cyber-Physical Systems",
        "Digital Design and Computer Architecture",
        "Introduction to Robotics: Mechanics and Control",
        "Introduction to Computational Complexity",
        "Mobile Robotics: Algorithms and Applications",
        "Cloud Computing: Concepts and Practices",
        "Principles of Computer Animation",
        "Introduction to Formal Verification",
        "Wireless Sensor Networks: Principles and Applications",
        "Introduction to Cryptographic Protocols",
        "Digital Systems Design: Principles and Practices",
        "Quantum Computing: Principles and Applications",
        "Computer-Aided Design and Manufacturing",
        "Introduction to Human-Robot Collaboration",
        "Evolutionary Computation: Principles and Applications",
        "Introduction to Computer Forensic Analysis",
        "Computer Architecture: Pipelining and Superscalar Techniques",
        "Introduction to Network Security",
        "Digital Image Processing: Algorithms and Applications",
        "Principles of Cyber-Physical Systems",
        "Introduction to Computational Linguistics",
        "Computer Graphics: Principles and Practices",
        "Advanced Topics in Machine Learning",
        "Introduction to Biometric Authentication",
        "Introduction to Wireless Communications",
        "Computational Geometry: Algorithms and Applications",
        "Introduction to Digital Control Systems",
        "Robotics and Automation: Principles and Practices",
        "Introduction to High-Performance Computing",
        "Introduction to Quantum Information Science",
        "Cyber-Physical Systems: Design and Implementation",
        "Introduction to Multimedia Systems",
        "Computer Vision: Principles and Practices",
        "Embedded Systems Programming: Concepts and Practices",
        "Introduction to Information Retrieval",
        "Introduction to Game Development",
        "Advanced Topics in Cryptography",
        "Digital System Design: Concepts and Practices",
        "Introduction to Virtual Reality",
        "Introduction to Computer Music Composition",
        "Introduction to Smart Grids",
        "Principles of Cyber-Physical Security"
    ]

    library.add_books(book_titles)

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


