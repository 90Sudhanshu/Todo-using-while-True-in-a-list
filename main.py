# Todo using while True in a list

todo = []

while True:
    user_action = input("Enter add, show, edit, complete exit: ")

    match user_action:
        case 'add':
            task = input("Enter the task to add: ")
            todo.append(task)

        case 'show':
            for i in todo:
                row = f"{i}"
                print(row)

        case 'edit':
            num = int(input("Enter the number to edit: "))
            new_todo = input("Enter the new todo: ")
            todo[num-1] =new_todo

        case 'complete':
            num = int(input("Enter the number to edit: "))
            todo.pop(num-1)

        case 'exit':
            break
