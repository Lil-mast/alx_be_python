def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.
    
    Args:
        numerator: The numerator (will be converted to float)
        denominator: The denominator (will be converted to float)
    
    Returns:
        float: The division result if successful
        str: Error message if division fails
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return result
        
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
        
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"