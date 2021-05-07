from pathlib import Path
import os


def save_to_file(file_name, text):
    """ A method to save input to a file.

    :param file_name: (str) The file name.
    :param text: (str) Input string obtained from GUI.
    :return: (str , str) Returns a string message and a string file path.
    """

    file = Path(file_name)

    if file.is_file():
        add_to_file = open(file, "a")
        add_to_file.write(f'\n{text}')
        add_to_file.close()
        return "Appended to file.", os.path.abspath(file)
    else:
        new_file = open(file, "x")
        new_file.write(text)
        new_file.close()
        return "Created a new file.", os.path.abspath(file)



