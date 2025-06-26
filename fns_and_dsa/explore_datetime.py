from datetime import datetime, timedelta

def display_current_datetime():
    """Demonstrates current datetime handling with proper formatting"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """Calculates future date with input validation and clean formatting"""
    if not isinstance(days, int):
        raise ValueError("Days must be an integer")
    
    current = datetime.now()
    future_date = current + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days} days: {formatted_future}")
    return future_date

def main():
    """Orchestrates the datetime demonstration with user interaction"""
    print("\n=== DateTime Module Demonstration ===")
    
    # Part 1: Current datetime
    current = display_current_datetime()
    
    # Part 2: Future date calculation
    try:
        days_input = int(input("\nEnter number of days to add: "))
        calculate_future_date(days_input)
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid integer.")

if __name__ == "__main__":
    main()