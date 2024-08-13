def get_todos(filepath='filetxt/todos.txt'): #default argument
    """
    Read a text file and return the list of to_do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
help(get_todos)
def write_todos(todos_arg, filepath='filetxt/todos.txt'): #default phải đứng sau parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("Hello")

if __name__ == "__main__": #đoạn code này sẽ không show trên file code chinh khi run
    print("Hello")
    print(get_todos())