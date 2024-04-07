def get_todos(filepath="todo.txt"): #argument filepath
    with open(filepath, 'r') as file_local:  #argument filepath
        todos_local = file_local.readlines()
        return todos_local

def write_todos(filepath="todo.txt"):
    with open(filepath, 'w') as file:
        file.writelines()