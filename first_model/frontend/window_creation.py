import PySimpleGUI as sg


def create_window():
    layout = [
        [sg.Text("A sample GUI")],
        [sg.Text("Enter your name: "), sg.Input(key='-NAME-')],
        [sg.Button("Save"), sg.Button("Exit")]
    ]

    return sg.Window("First Model", layout, finalize=True)


def pop(msg):
    """ A method to create a pop up

    :param msg: (str) The content of the pop up.
    :return: A PySimpleGUI object
    """
    return sg.popup(msg)
