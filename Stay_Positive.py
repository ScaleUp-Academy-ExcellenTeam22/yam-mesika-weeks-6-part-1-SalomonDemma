def get_positive_numbers() -> list:
    """
    A function that receives input from the user using input.
    User n will be asked to enter a series of numbers separated by a comma.
    The function will return all the positive numbers that the user entered,
    as a list of int numbers.
    """
    inp_num = input('Enter a series of numbers separated by a comma:\n').split(',')
    lst = list(map(lambda num: int(num), inp_num))
    return [num for num in lst if num > 0]


if __name__ == "__main__":
    print(get_positive_numbers())
