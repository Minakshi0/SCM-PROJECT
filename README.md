Team Members:

Minakshi Sharma   2310990573  , Mohit Kumar   2310990574 ,  Monika Meena   2310990575

Library Management System

This is a Python-based library management system that allows users to manage books, issue them to borrowers, and return them. The system is designed to be easy to use and can be integrated into existing library setups.

Features

•	Add books to the library inventory.
•	Display available books with their IDs, titles, and statuses.
•	Issue books to borrowers, updating their status and recording the lender's name and issue date.
•	Return books to the library, updating their status and clearing borrower information.

Requirements

Python 3.x

Algorithm for the python code

The algorithm below provides a structured approach to understanding the functionality and flow of the Library Management System implemented in the provided Python code.

Book Class:

Create a class named Book.
Initialize the Book class with attributes such as book_id, title, status, lender_name, and lend_date.
Set the initial values of status, lender_name, and lend_date to "Available", "", and "" respectively.

Library Class:

Create a class named Library.
Initialize the Library class with attributes such as name and an empty dictionary books to store book objects.
Implement a method named add_books to add books to the library inventory.
Implement a method named display_books to display the list of available books with their IDs, titles, and statuses.
Implement a method named issue_book to issue a book to a borrower, updating its status, lender name, and lend date.
Implement a method named return_book to return a book to the library, updating its status and clearing lender information.

Main Program:

Create an instance of the Library class with the name "Python's Library".
Define a list of book titles.
Add the book titles to the library using the add_books method.
Run a continuous loop to display a menu and handle user input:
Display options to display books, issue a book, return a book, or exit the program.
Based on the user's choice, call the respective methods of the Library class.
Exit the loop when the user chooses to exit the program.

User Interface:

Display a welcome message to the user.
Display a menu with options to interact with the library management system.
Prompt the user to enter their choice.
Prompt the user for additional inputs such as book ID, lender name, etc., based on their choice.

Error Handling:

Check for invalid user inputs and provide appropriate error messages.
Handle cases such as invalid book IDs, unavailable books, etc.

Datetime Module Usage:

Import the datetime module to work with dates and times.
Use the strftime method of the datetime module to format the current date and time.

