# Ask the user to inpujt a number

try:
    number = int(input("Enter a number to generate its multiplication table: "))
except ValueError:
    print("Error: Please enter a valid integer!")
    exit(1)
    
 # Generate the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")