import sys
from robust_division_calculator import safe_divide

def main():
    # Check if two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 2")
        return
    
    # Get numerator and denominator from command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform the division
    success, result = safe_divide(numerator, denominator)
    
    # Display results
    if success:
        print(f"Result: {result:.4f}")  # Display with 4 decimal places
    else:
        print(result)

if __name__ == "__main__":
    main()