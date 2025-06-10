# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_FACTOR) * 5/9

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Is this Celsius or Fahrenheit? (C/F): ").upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C = {converted:.2f}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F = {converted:.2f}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()