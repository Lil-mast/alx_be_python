# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings using formula
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05 
projected_savings = annual_savings + interest

# Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the results
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Your projected annual savings, including interest, are: {projected_savings:.2f}")