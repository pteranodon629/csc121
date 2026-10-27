# Kevin K. Lux-Sullivan
# 23Sep2026
# 27Oct2026: KLS: Added load_books(), format_book, with CSV support
# CSC121 Week 6 Assignment
from csv import DictReader
from csv import DictWriter


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

    with open("books.csv", "a", newline="", encoding="utf-8") as outfile:
        fieldnames = ["title", "author", "pages", "hours"]
        writer = DictWriter(outfile, fieldnames)
        writer.writerow(book)


def view_books(library):
    if len(library) < 1:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            print(format_book(library[i], i + 1))


def main():
    header()
    library = []
    library = load_books(library)

    while True:
        dashboard()
        # clean input with strip() and lower()
        choice = input("> ").strip().lower()
        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        else:
            # handle off-menu inputs
            print("Sorry, that option isn't available.")


def load_books(library):
    try:
        with open("books.csv", "r") as csvfile:
            reader = DictReader(csvfile)
            i = 0
            for row in reader:
                library.append(row)
            return library

    except FileNotFoundError:
        # There is no file, so create a new one with header only
        with open("books.csv", "x", newline="", encoding="utf-8") as newfile:
            fieldnames = ["title", "author", "pages", "hours"]
            writer = DictWriter(newfile, fieldnames)
            writer.writeheader()
            return library


def format_book(book, number):
    return f"{number}. '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} hours to read)"


if __name__ == "__main__":
    main()
