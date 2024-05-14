to_do_list = []

try:
    with open("todo_list.txt", "r") as file:
        for line in file:
            to_do_list.append(line.strip())
except FileNotFoundError:
    print("No saved items found")

while True:
    print("================================================")
    print("Welcome to the to-do list application")
    print()
    print("Here is your current to-do list:")
    index = 1
    for task in to_do_list:
        print(f"{index}: {task}")
        index += 1
    print()

    user_choice = input("What is your desired action [input 'a' to add a task, or input 'x' to exit the program, input 'r' to remove a task from the list]: ")
    if user_choice.upper() == "A":
        task_input = input("What task would you like to add? ")
        to_do_list.append(task_input)
    if user_choice.upper() == "R":
        item_number = int(input("What task would you like to remove? "))
        if item_number > 0 and item_number <= len(to_do_list):
            to_do_list.pop(item_number - 1)
        else:
            print("Invalid item number")
        continue
    if user_choice.upper() == "X":
        with open("todo_list.txt", "w") as file:
            for todo in to_do_list:
                file.write(f"{todo}\n")
        break