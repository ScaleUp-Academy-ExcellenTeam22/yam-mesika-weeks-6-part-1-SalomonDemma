def get_positive_numbers(list_of_str_numbers: list) -> list:
    """
    The function receives a list of strings of numbers.
    The function converts the strings of numbers to integers and returns
    a list of the positive numbers from the list of numbers that the function
    converted to integers.
    :param list_of_str_numbers: A list of strings of numbers.
    :return: A list of the positive numbers.
    """

    list_of_int_numbers = list(map(lambda num: int(num), list_of_str_numbers))
    return [num for num in list_of_int_numbers if num > 0]


if __name__ == "__main__":
    print(get_positive_numbers(input('Enter a series of numbers separated by a comma:\n').split(',')))
