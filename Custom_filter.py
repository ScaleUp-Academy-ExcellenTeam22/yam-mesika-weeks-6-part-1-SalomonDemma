def my_filter(function: callable, iterable: iter) -> iter:
    """
    Filter creates a new iterable and returns it.
    The iterable includes only those elements for which the transmitted function
    returned a value equivalent to True.
    :param function: Function
    :param iterable: Iterable
    :return: Iterable of filtered item.
    """
    return iter([item for item in iterable if function(item)])


def is_mature(age: float) -> bool:
    """
    The function receives an age and checks if the age is over 18.
    :param age: An float number.
    :return: "True" if mature "False" if not.
    """
    return age >= 18


if __name__ == "__main__":
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    print(list(my_filter(is_mature, ages)))
