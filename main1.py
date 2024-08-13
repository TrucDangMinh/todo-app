#todos = [] Không cần nữa vì đã export ra txt

#from functions import get_todos, write_todos (không cần thêm gì vào call function)

from module import functions
import time

now = time.strftime("%Y")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        if todo == '\n':
            print("Please add something")
        else:
            todos = functions.get_todos()

            todos.append(todo)

            # có thể dùng call function default bằng cách này hoặc
            #write_todos(filepath='filetxt/todos.txt', todos_arg=todos)
            #write_todos(todos) vì filepath là default nên không cần điền
            functions.write_todos(todos_arg=todos, filepath='filetxt/todos.txt')

    elif user_action.startswith("show"):
        # # Vì không còn todos (exported ra txt) sẽ gây ra lỗi nên phải read file lấy data
        # file = open('test1/todos.txt', 'r')
        #
        # # todos lúc đầu là list, nên dùng readlines() sẽ cho datatype là list giống ban đầu
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        #5 xóa khoảng trắng (\n) khi show ra màn hình, KHÔNG DÙNG VÌ DÀI DÒNG
        # news1_todos = []
        # for ishow in todos:
        #     news_item = ishow.strip()
        #     news1_todos.append(news_item)

        #5 xóa khoảng trắng (\n) khi show ra màn hình, LIST COMPREHENSION không dùng
        # news_item = [ishow.strip() for ishow in todos]

        #5 xóa khoảng trắng (\n) khi show ra màn hình, DÙNG CÁCH NÀY VÌ GỌN
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}: {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            # yêu cầu: gõ 'edit + số', không cần làm phải input như bước # 6
            # 6 number = int(input("Enter number to edit: "))
            # mỏ file và đọc, dtt:list
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            # thay thế element
            news_todo = input("Type your content: ")
            todos[number] = news_todo + '\n'

            # write vào file
            functions.write_todos(todos)
        except ValueError:
            print("Please enter a number of todos.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Please type complete and a number in the list.")
        except ValueError:
            print("Please type complete and a number to complete.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye!")