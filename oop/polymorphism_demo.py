# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area calculated as length × width
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """Initialize circle with radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area calculated as π × radius²
        """
        return math.pi * (self.radius ** 2)