import PySimpleGUI as sg


def create_window():
    """ A method to create a PySimpleGUI window.

    :return: (obj) Returns a PySimpleGUI object.
    """
    layout = [
        [sg.Text("A sample GUI")],
        [sg.Text("Select file to edit: ", size=(15, 1)), sg.Input(size=(50, 1), key='-EXISTING_FILE-'), sg.Button("New File", key='-NEW-')],
        [sg.Text("Write your file")],
        [sg.Multiline(key='-TEXT-', autoscroll=True, size=(67, 10))],
        [sg.Button("Save"), sg.Button("Exit")]
    ]

    return sg.Window("First Model", layout, finalize=True)


def pop(msg):
    """ A method to create a popup.

    :param msg: (str) The content of the pop up.
    :return: A PySimpleGUI object
    """
    return sg.popup(msg)

def new_file():
    """

    :return:
    """
    layout = [
        [sg.Text("Enter file name: "), sg.Input(key='-NEW_FILE_NAME-')],
        [sg.Button("Ok"), sg.Button("Cancel")]
    ]

    return sg.Window("Create File", layout, finalize=True)

