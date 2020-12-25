# class Library
# display books
# add book
# lend book (who owns the book if not present)
# return book in the library
# constructor HarryLibrary=Library(listofbooks, libraryname)
# dictionary key-pair ----> (books-name of person)

# create a main function and run a infinite while loop asking user for


class Library:

    def __init__(self, booklist, name):
        self.dict1 = booklist
        self.dict2 = {}
        self.name = name

    def displaybook(self):
        for i in self.dict1:
            print(i, end="\n")

    def addbook(self, added_book):
        dict1_len = len(self.dict1)
        self.dict1[dict1_len + 1] = added_book
        print(f"Book {added_book} added to the library")

    def lendbook(self, book_key, username):
        if book_key in self.dict2:
            print(f"Sorry!Book not present,currently owned by {self.dict2[book_key]}")
        else:
            self.dict2[book_key] = username

    def returnbook(self, returned_book):
        self.dict2.pop(returned_book)
        print(f"Book {returned_book} has been returned to the library")


kartik = Library({"Gita", "Harry Potter", "The Alchemist", "Python 3", "Basics of C++"}, "Kartikeya")

if __name__ == '__main__':
    while True:
        print(f"\n\nWelcome to {kartik.name}'s Library management system")
        print("1. To display all books")
        print("2. To add a book")
        print("3. To lend a book to the user")
        print("4. To return the book")
        user_choice = int(input("Enter your choice to continue"))
        if user_choice == 1:
            kartik.displaybook()
        elif user_choice == 2:
            book = input("\nEnter the book to be added")
            kartik.addbook(book)
        elif user_choice == 3:
            book = input("\nEnter the name of book selected")
            username = input("\nEnter the user's name")
            kartik.lendbook(book, username)
        elif user_choice == 4:
            book = input("Enter the book to be returned")
            kartik.returnbook(book)
        else:
            print("Please enter a valid choice")

        choice = input("Press c to continue,Press any else key to quit")
        if choice == "c":
            continue
        else:
            break
