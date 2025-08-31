# library_system.py
class Book:
    """Base class representing a book with title and author."""
    
    def __init__(self, title: str, author: str):
        """Initialize book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book with file size."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize eBook with title, author, and file size.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): File size in kilobytes
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book with page count."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize print book with title, author, and page count.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): Number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books using composition."""
    
    def __init__(self):
        """Initialize library with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library collection.
        
        Args:
            book: Instance of Book, EBook, or PrintBook
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print(f"Error: {book} is not a valid Book instance")
    
    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\n=== Library Collection ===")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("==========================\n")