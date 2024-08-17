from module import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",
                         key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(key='todos',
                      values=functions.get_todos(),
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            """ Logic:
            - Lấy 2 gia tri moi va cu
            - Mo file chua list replace
            """
            # Get value and convert it to string
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            # Open file
            todos = functions.get_todos()

            # Get index of old string
            index = todos.index(todo_to_edit)

            # Replace old value by new one
            todos[index] = new_todo

            # Save new value to file
            functions.write_todos(todos)

            # Make it real-time
            window['todos'].update(values=todos)

        # Show selection and make it real-time
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()