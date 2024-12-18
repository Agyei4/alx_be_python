#script to acts as a daily reminder for tracking tasks

#accepting inputs from user i.e. name of task, priority,if it is time bound
name_of_task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#condtional options
match priority:
    case "high":
        priority_message ="high priority task"
    case "medium":
        priority_message ="medium priority task"
    case "low":
        priority_message ="low priority task"
    case _:
        print("an undefined priority task")

while True:
    if time_bound == "yes":
        time_bound_message = " that requires immediate attention today!"
        break
    elif time_bound == "no":
        time_bound_message = ". Consider completing it when you have free time."
        break
    else:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound == "q":
            time_bound_message = ""
            break

dialy_message = f"'{name_of_task}' is a {priority_message}{time_bound_message}"

print(dialy_message)

