# Kevin K. Lux-Sullivan
# 23Sep2026
# CSC121 Week 6 Assignment

def header():
    """Prints  
        40 '='
          📚  YOUR LIBRARY
        40 '='
        """
    print("=" * 40)
    print("  📚  YOUR LIBRARY")
    print("=" * 40)

def dashboard():
    print()
    print("What would you like to do?")
    print()
    print("1) View books")
    print("2) Add a book")
    print()
    print("q) Quit")
    print()

def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    return round(pages / 40, 1)


def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    book = {"title": title, "author": author, "pages": pages, "hours": hours}
    
    library.append(book)

    print("Book added: ")
    print(f"'{book["title"]}' by {book["author"]} -- approx. {hours} hours to read")


def view_books(library):
    if len(library) < 1:
        print("Your library is empty. Add a book first!")
    else:
        i = 1
        for b in library:
            print(f"{i}.'{b["title"]}' by {b["author"]} -- approx. {b["hours"]} hours to read")
            i += 1

def main():
    header()
    library = []
    
    while True:
        dashboard()
        # clean input with strip() and lower()
        choice = input("> ").strip().lower()
        if choice == '1':
            view_books(library)
        elif choice == '2':
            add_book(library)
        elif choice in ('q', 'quit', 'exit'):
            print("Goodbye!")
            break
        else:
            # handle off-menu inputs
            print("Sorry, that option isn't available.")


if __name__ == "__main__":
    main()