task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task "
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task "
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task "
    case _ :
        reminder = f"Reminder: '{task}' has an undefined priority "

if time_bound == "yes":
    reminder += "that requires immediate attention today! "
else:
    reminder += "consider completing it when you have free time"
print(reminder)