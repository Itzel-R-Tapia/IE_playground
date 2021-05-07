from first_model.backend.manager import save_to_file
from first_model.frontend.window_creation import create_window, pop, new_file
import PySimpleGUI as sg


def model_gui():
    """ A method to display a simple GUI.

    """

    main_window, new_file_window = create_window(), None
    file = None
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Cancel":
            window.close()
            if window == new_file_window:
                new_file_window = None
            elif window == main_window:
                break
        elif event == '-NEW-' and not new_file_window:
            new_file_window = new_file()
        elif event == 'Ok':
            file = values['-NEW_FILE_NAME-']
            window.close()
        elif event == 'Save':
            if file is None:
                file = values['-EXISTING_FILE-']
            window.close()
            break
    if file:
        msg, file_path = save_to_file(file, values['-TEXT-'])
        pop(f'{msg} \n File path: {file_path}')
