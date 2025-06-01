# Prompt the user for task details
task = input("Enter the task you want to be reminded of: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

deadline = None

def get_priotity():
    while True:
        priority = input("Enter the priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            return priority
        else:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def is_time_bound():
    while True:
        time_bound = input("Is the task time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            return time_bound
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to get deadline
def get_deadline():
    while True:
        deadline = input("Enter the deadline (YYYY-MM-DD HH:MM): ")
        try:
            from datetime import datetime
            datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            return deadline
        except ValueError:
            print("Invalid date format. Please use  YYYY-MM-DD HH:MM format.")

# Main program
def main():
    task = input("Enter the task: ")
    priority = get_priotity()
    time_bound = is_time_bound()

    deadline = None
    if time_bound:
        deadline = get_deadline()

# Process task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention."
        if deadline:
            reminder += f" by {deadline}!"
        else:
            reminder += " today!"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if deadline:
            reminder = f" Please complete it by {deadline}."
        else:
            reminder += "Consider completing it soon."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
        if deadline:
            reminder += f" You have free time until {deadline}."
        else:
            reminder += " You can do this when you have free time."
    case _:
        reminder = "Invalid priority level entered."

print(reminder)

if __name__ == "__main__":
    main()