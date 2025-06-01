# Ask the user to inpujt a number
number = int(input("Enter a number to generate its multiplication table: "))

 # Generate the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")