def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.
    
    Args:
        numerator: The numerator (will be converted to float)
        denominator: The denominator (will be converted to float)
    
    Returns:
        str: Formatted division result or error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        
        # Format the successful result as specified
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"