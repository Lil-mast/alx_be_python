# class_static_methods_demo.py
class Calculator:
    """A class demonstrating the use of static methods and class methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and display calculation type.
        
        Args:
            cls: The class reference
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b