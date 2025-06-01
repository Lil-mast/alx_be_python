# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize variables
deadline = None

# Check if the task is time-boound
if time_bound == "yes":
    deadline = input("Deadline (YYYY-MM-DD HH:MM): ")

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