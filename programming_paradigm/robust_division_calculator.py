def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.
    
    Args:
        numerator: The numerator (dividend)
        denominator: The denominator (divisor)
        
    Returns:
        tuple: (success status, result/error message)
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return (True, result)
    
    except ZeroDivisionError:
        return (False, "Error: Division by zero is not allowed.")
    except ValueError:
        return (False, "Error: Both inputs must be numeric.")
    except Exception as e:
        return (False, f"Error: An unexpected error occurred - {str(e)}")