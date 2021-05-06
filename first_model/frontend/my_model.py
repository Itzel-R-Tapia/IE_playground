from first_model.backend.manager import save_name
from first_model.frontend.window_creation import create_window, pop


def model_gui():
    """ A method to display a simple GUI.

    """

    window = create_window()

    while True:
        event, values = window.read()
        if event == "Exit":
            break;
        save_name(values['-NAME-'])
        pop("Saved!")
