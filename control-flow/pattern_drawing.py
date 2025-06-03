# Prompt the user fo rthe size of the match pattern
while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Initialize the row counter
row = 0

while row < size:
    for col in range(size):
        print("*", end='')

    print() # Move to the next line after printing a row
    row += 1  # Increment the row counter   
