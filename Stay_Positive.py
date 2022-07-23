def get_positive_numbers(list_of_str_numbers: list) -> list:
    """
    A function that receives input from the user using input.
    User n will be asked to enter a series of numbers separated by a comma.
    The function will return all the positive numbers that the user entered,
    as a list of int numbers.
    """
    list_of_int_numbers = list(map(lambda num: int(num), list_of_str_numbers))
    return [num for num in list_of_int_numbers if num > 0]


if __name__ == "__main__":
    print(get_positive_numbers(input('Enter a series of numbers separated by a comma:\n').split(',')))
