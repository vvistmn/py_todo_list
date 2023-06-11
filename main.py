from modules import functions
from modules.functions import write_todos
import time

text = """
ЭТО

МНОГОСТРОЧНАЯ

СТРОКА
"""
print(text)

while True:
    current_date = time.strftime('%b %d, %Y %H:%M:%S')
    print(f"It is {current_date}")
    user_action = input("Type add, edit, show, complete or exit: ").lower().strip()

    todo_list = functions.get_todos()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add') or user_action.startswith('new'):
        if user_action == 'add' or user_action == 'new':
            todo = input("Enter a todo: ") + "\n"
        else:
            todo = user_action[4:] + '\n'

        todo_list.append(todo)

        write_todos(todo_list)
    # elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            if user_action == 'edit':
                for index, item in enumerate(todo_list):
                    item = item.title().strip('\n')
                    row = f"{index + 1}: {item.title()}"
                    print(row)

                number = int(input("Number of the todo to edit: "))
            else:
                number = int(user_action[5:])
        except ValueError:
            print('Your command is not valid.')
            continue
        except IndexError:
            print('There is no item with that number.')
            continue

        new_todo = input("Enter new todo: ")
        todo_list[number - 1] = new_todo + '\n'

        write_todos(todo_list)
    # elif 'show' in user_action or 'display' in user_action:
    elif user_action.startswith('show') or user_action.startswith('display'):
        # new_todo_list = [item.strip('\n') for item in todo_list]
        # print(new_todo_list)

        for index, item in enumerate(todo_list):
            item = item.title().strip('\n')
            row = f"{index + 1}: {item}"
            print(row)

        print(f"Length is: {len(todo_list)}")
    # elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        try:
            if user_action == 'complete':
                for index, item in enumerate(todo_list):
                    item = item.title().strip('\n')
                    row = f"{index + 1}: {item}"
                    print(row)

                number = int(input("Number of the todo to complete: "))
            else:
                number = int(user_action[9:])
        except ValueError:
            print('Your command is not valid.')
            continue
        except IndexError:
            print('Your command is not valid.')
            continue

        todo_completed = todo_list.pop(number - 1)
        row = f"Todo completed - {todo_completed}"
        print(row)

        write_todos(todo_list)
    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        print('Thanks! Bye!')
        break
    else:
        print('Hey, you entered an unknown command')
