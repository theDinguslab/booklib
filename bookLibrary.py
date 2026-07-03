## Absolutely NO LLMs or artificial intelligence bots were used in the creation of this program.
## This code was written by myself in VSC with the fantastic assistance of the references listed below:
##
## https://docs.python.org/3/library/datetime.html
## https://www.w3schools.com/python/python_arguments.asp
## https://docs.python.org/3/tutorial/controlflow.html
## https://www.w3schools.com/python/python_match.asp
## https://www.pluralsight.com/labs/codeLabs/guided-build-a-library-system-with-python
## https://www.krython.com/tutorial/python/oop-project-library-management-system
## https://stackoverflow.com/questions/42472228/simple-library-management-system-using-python






## INITIAL LIBRARY PER INSTRUCTIONS  
from datetime import date
 
library = {
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "isbn": "9780451524935"
    },
    "Dune": {
        "author": "Frank Herbert",
        "year": 1965,
        "isbn": "9780441172719"
    },
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "isbn": "9780547928227"
    }
}
 
## MAIN MENU
def display_menu():
    print("\n--- Personal Library Management System ---")
    print("1. Add a book")
    print("2. Update a book's author")
    print("3. Update a book's publication year")
    print("4. Search for a book by title")
    print("5. Delete a book")
    print("6. Display all books (sorted by title)")
    print("7. Exit")
 
## ADD NEW BOOK
def add_book():
    print("\n-- Add a Book --")
 
    ## VALIDATE BOOK TITLE
    while True:
        title = input("Enter book title: ").strip()
        if title == "":
            print("Error: Title cannot be blank.")
        elif title in library:
            print("Error: A book with that title already exists.")
        else:
            break
 
    ## VALIDATEW BOOK AUTHOR
    while True:
        author = input("Enter author name: ").strip()
        if author == "":
            print("Error: Author cannot be blank.")
        else:
            break
 
    ## VALIDATE RELEASE YEAR
    current_year = date.today().year
    while True:
        year_input = input(f"Enter publication year (1000 - {current_year + 1}): ").strip()
        if not year_input.isdigit():
            print("Error: Year must be a number.")
        else:
            year = int(year_input)
            if year < 1000 or year > current_year + 1:
                print(f"Error: Year must be between 1000 and {current_year + 1}.")
            else:
                break
 
    ## VALIDATE ISBN 
    while True:
        isbn = input("Enter ISBN (numeric, at least 10 digits): ").strip()
        if not isbn.isdigit():
            print("Error: ISBN must be numeric.")
        elif len(isbn) < 10:
            print("Error: ISBN must be at least 10 characters long.")
        else:
            break
 
    ## ADD BOOK TO LIBRARY
    library[title] = {
        "author": author,
        "year": year,
        "isbn": isbn
    }
    print(f"'{title}' has been added to the library.")
 
## UPDATE AUTHOR IN DATABASE
def update_author():
    print("\n-- Update a Book's Author --")
 
    title = input("Enter the title of the book to update: ").strip()
 
    ## CHECK IF BOOK EXISTS IN DATABASE 
    if title not in library:
        print(f"Error: '{title}' was not found in the library.")
        return
 
    ## VALIDATE NEW AUTHOR ENTREY
    while True:
        new_author = input(f"Enter new author for '{title}': ").strip()
        if new_author == "":
            print("Error: Author cannot be blank.")
        else:
            break
 
    library[title]["author"] = new_author
    print(f"Author for '{title}' has been updated to '{new_author}'.")
 
## UPDATE YEAR IN DATABASE
def update_year():
    print("\n-- Update a Book's Publication Year --")
 
    title = input("Enter the title of the book to update: ").strip()
 
    ## CHECK IF BOOK EXISTS IN DATABASE
    if title not in library:
        print(f"Error: '{title}' was not found in the library.")
        return
 
    ## VALIDATE RELEASE YEAR
    current_year = date.today().year
    while True:
        year_input = input(f"Enter new publication year (1000 - {current_year + 1}): ").strip()
        if not year_input.isdigit():
            print("Error: Year must be a number.")
        else:
            year = int(year_input)
            if year < 1000 or year > current_year + 1:
                print(f"Error: Year must be between 1000 and {current_year + 1}.")
            else:
                break
 
    library[title]["year"] = year
    print(f"Publication year for '{title}' has been updated to {year}.")
 
## SEARCH DATABASE FOR A BOOK
def search_book():
    print("\n-- Search for a Book --")
 
    title = input("Enter the title to search for: ").strip()
 
    if title in library:
        book = library[title]
        print("\nBook found:")
        print(f"Title:  {title}")
        print(f"Author: {book['author']}")
        print(f"Year:   {book['year']}")
        print(f"ISBN:   {book['isbn']}")
        print("------------------------")
    else:
        print(f"'{title}' was not found in the library.")
 
## DELETING BOOKS FROM DATABASE
def delete_book():
    print("\n-- Delete a Book --")
 
    title = input("Enter the title of the book to delete: ").strip()
 
    if title not in library:
        print(f"Error: '{title}' was not found in the library.")
        return
 
    ## CONFIRMATION
    confirmation = input(f"Are you sure you want to delete '{title}'? (Y/N): ").strip().upper()
 
    if confirmation == "Y":
        del library[title]
        print(f"'{title}' has been deleted from the library.")
    else:
        print("Delete operation cancelled.")
 
## DISPLAY ENTIRE BOOK DATABASE
def display_all_books():
    print("\n-- All Books (Sorted by Title) --")
 
    if len(library) == 0:
        print("The library is empty.")
        return
 
    ## SORT THE LIBRARY KEYS
    sorted_titles = sorted(library.keys())
 
    for title in sorted_titles:
        book = library[title]
        print(f"Title:  {title}")
        print(f"Author: {book['author']}")
        print(f"Year:   {book['year']}")
        print(f"ISBN:   {book['isbn']}")
        print("------------------------")
 
## DISPLAY MENU & HANDLE CHOICES MADE BY USER THAT COULD CREATE A LOOP
def main():
    print("Welcome to the Personal Library Management System!")
 
    while True:
        display_menu()
 
        choice = input("\nEnter your choice (1-7): ").strip()
 
        if choice == "1":
            add_book()
        elif choice == "2":
            update_author()
        elif choice == "3":
            update_year()
        elif choice == "4":
            search_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            display_all_books()
        elif choice == "7":
            # Ask for exit confirmation
            confirm_exit = input("Are you sure you want to exit? (Y/N): ").strip().upper()
            if confirm_exit == "Y":
                print("Goodbye!")
                break
            else:
                print("Returning to menu...")
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")
 
 
#RUN PROGRAM
main()