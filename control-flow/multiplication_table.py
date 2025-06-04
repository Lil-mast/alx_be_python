# Prompt the user to enter a number
while True:
    try:
        number = int(input("Enter a number to generate its multiplication table: "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Error: Please enter a valid integer!")

# Generate and print the multiplication table
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")