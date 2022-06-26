def get_letters() -> list:
    """
    A function that returns the list of all characters between a and z and between A and Z.
    """
    acb_list = list(map(lambda low_c: chr(low_c), range(ord('a'), ord('z') + 1)))  # adding the lower letter
    acb_list += list(map(lambda low_c: chr(low_c), range(ord('A'), ord('Z') + 1)))  # adding the upper letter
    return acb_list


if __name__ == "__main__":
    print(get_letters())
