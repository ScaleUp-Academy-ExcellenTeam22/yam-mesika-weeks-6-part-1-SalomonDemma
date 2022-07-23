import string


def get_letters() -> list:
    """
    A function that returns the list of all characters between a and z and between A and Z.
    """
    return list(string.ascii_letters)


if __name__ == "__main__":
    print(get_letters())
