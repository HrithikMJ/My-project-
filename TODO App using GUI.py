import PySimpleGUI as Sg
def add_task(value):
    task = value['task_name']
    if task != "":
        if values[0]:
            to_do_work.insert(0, task+" ^very important")
        elif values[1]:
            to_do_work.insert(int(len(to_do_work)/2)+1, task+" ^less important")
        elif values[2]:
            to_do_work.insert(len(to_do_work), task+" ^not important")

    window.FindElement('task_name').Update(value="")
    window.FindElement('to_do_work').Update(values=to_do_work)
    window.FindElement('add_save').Update('Add')
def edit_tasks(value):
    try:
        edit_val = value['to_do_work'][0]
        window.FindElement('task_name').Update(value=edit_val)
        todowork.remove(edit_val)
        window.FindElement('add_save').Update('Save')
    except:
        pass


def clear_tasks(value):
    try:
        clear_val = value['to_do_work'][0]
        todowork.remove(clear_val)
        window.FindElement('to_do_work').Update(values=to_do_work)
    except:
        pass

def clear_all():
    try:
        for i in range(len(to_do_work)):
            del to_do_work[i]
        window.FindElement("to_do_work").Update(values=to_do_work)
    except:
        pass
Sg.theme("BrightColors")
font_name = ' Verdana  '
font_size = 20
layout = [
    [
        Sg.Text("Enter the work in the below box", font=(font_name, font_size))],
        [Sg.InputText("", font=(font_name, font_size), size=(20, 1), border_width=0, key="task_name"),
    ],

    [
        Sg.Text("My work      ", font=(font_name, font_size))],
        [Sg.Radio("very important", 10)],
        [Sg.Radio("less important", 10, default=True)],
       [ Sg.Radio("not important", 10)
    ],

    [
        Sg.Button("Add", font=(font_name, font_size), border_width=8, key="add_save"),
        Sg.Button("Edit", font=(font_name, font_size), border_width=8),
        Sg.Button("Clear", font=(font_name, font_size), border_width=8),
        Sg.Button("Clear All", font=(font_name, font_size), border_width=8)
    ],

    [
        Sg.Listbox(values=[], size=(40, 10), font=(font_name, font_size), key='to_do_work')
    ]

]

to_do_work = []


window = Sg.Window("My work", layout)

while True:
    event, values = window.Read()
    if event == 'add_save':
        add_task(values)
    elif event == 'Edit':
        edit_tasks(values)
    elif event == 'Clear':
        clear_tasks(values)
    elif event == "Clear All":
        clear_all()
    else:
        break

window.Close()
