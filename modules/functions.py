FILEPATH = 'todos.txt' # Константа


def get_todos(filepath=FILEPATH):
    """
    Документация функции питона
    """
    try:
        with open(filepath, 'r') as file_local:
            todos = file_local.readlines()
    except FileNotFoundError:
        todos = []

    return todos


def write_todos(todos, filepath=FILEPATH):
    """ Документация функции питона """
    with open(filepath, 'w') as file:
        file.writelines(todos)


print(__name__)
if __name__ == '__main__':
    print(help(get_todos))
    print(help(write_todos))