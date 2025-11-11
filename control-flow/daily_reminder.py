# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate priority input
while priority not in ["high", "medium", "low"]:
    priority = input("Priority (high/medium/low): ").lower()

# Validate time-bound input
while time_bound not in ["yes", "no"]:
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        base_reminder = f"'{task}' is a high priority task"
    case "medium":
        base_reminder = f"'{task}' is a medium priority task"
    case "low":
        base_reminder = f"'{task}' is a low priority task"

# Add time-bound information
if time_bound == "yes":
    print(f"Reminder: {base_reminder} that requires immediate attention today!")
else:
    print(f"Reminder: {base_reminder}. Consider completing it when you have free time.")
