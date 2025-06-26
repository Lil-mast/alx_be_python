# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using global factor"""
    try:
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        if celsius < -273.15:  # Absolute zero check as literal value
            raise ValueError("Temperature below absolute zero")
        return celsius
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using global factor"""
    try:
        if celsius < -273.15:  # Absolute zero check as literal value
            raise ValueError("Temperature below absolute zero")
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_user_input() -> tuple:
    """Get and validate user input with proper error handling"""
    temp_input = input("Enter temperature (e.g., '32 C' or '89 F'): ").strip().upper()
    
    try:
        value, unit = temp_input[:-1], temp_input[-1]
        temp_value = float(value)
        
        if unit not in ('C', 'F'):
            raise ValueError("Invalid unit. Use 'C' or 'F'.")
            
        return temp_value, unit
        
    except (ValueError, IndexError):
        raise ValueError("Invalid format. Use format like '32 C' or '89 F'.")

def main():
    """Main execution flow with user interaction"""
    print("\n=== Temperature Conversion Tool ===")
    print(f"Global Conversion Factors: F→C={FAHRENHEIT_TO_CELSIUS_FACTOR:.2f}, C→F={CELSIUS_TO_FAHRENHEIT_FACTOR:.2f}\n")
    
    try:
        temp_value, unit = get_user_input()
        
        if unit == 'C':
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C = {converted:.2f}°F")
        else:
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F = {converted:.2f}°C")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()