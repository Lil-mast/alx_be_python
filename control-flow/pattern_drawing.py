# Prompt the user fo rthe size of the match pattern
size = int(input("Enter the size of the pattern"))

# Initialize the row counter
row = 0

while row < size:
    for col in range(size):
        print("*", end='')

    print() # Move to the next line after printing a row
    row += 1  # Increment the row counter