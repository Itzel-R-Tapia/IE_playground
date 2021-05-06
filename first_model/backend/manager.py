def save_name(name):
    """ A method to save input to a file.

    :param name:
    :return:
    """
    file = open("test_file.txt", "x")
    file.write(name)
    file.close()