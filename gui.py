from module import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",
                         key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(key='todos',
                      values=functions.get_todos(),
                      enable_events=True,
                      size=[45,10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button('Exit')
layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window("My To-Do App",
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            """ Logic:
            - Lay 2 gia tri moi va cu
            - Mo file chua list replace
            """
            try:
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
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))

        case "Exit":
            break
        # Show selection and make it real-time
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WINDOW_CLOSED:
            break
            # break hoac exit neu muon dung hoan toan

window.close()