def my_filter(function: callable, iterable: iter) -> iter:
    """
    Filter creates a new iterable and returns it.
    The iterable includes only those elements for which the transmitted function
    returned a value equivalent to True.
    :param function: Function
    :param iterable: Iterable
    :return: Iterable of filtered item.
    """
    filtered = []
    for item in iterable:
        if function(item):
            filtered.append(item)
    return iter(filtered)


if __name__ == "__main__":
    pass
