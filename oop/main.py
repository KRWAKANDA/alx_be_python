from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)        # __str__ is called
    print(repr(my_book))  # __repr__ is called

    del my_book           # __del__ is triggered

if __name__ == "__main__":
    main()
