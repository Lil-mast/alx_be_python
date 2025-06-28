class Book:
    """A class representing a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    @property
    def is_checked_out(self):
        """Get the current checkout status of the book."""
        return self._is_checked_out
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned/available."""
        self._is_checked_out = False


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library's collection.
        
        Args:
            book (Book): The book to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it's available.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """Return a book by title if it was checked out.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_checked_out:
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if not book.is_checked_out]
        
        if not available_books:
            print("No books currently available in the library.")
            return
            
        print("Available books:")
        for book in available_books:
            print(f"- '{book.title}' by {book.author}")