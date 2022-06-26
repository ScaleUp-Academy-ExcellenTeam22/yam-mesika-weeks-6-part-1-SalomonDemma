import time


def timer(f: callable, *args) -> float:
    """
    A function that receives as a function a function and other parameters.
    The timer function will measure how long a function f ran when the same
    parameters are passed to it.
    :param f: Function
    :param args: Parameters for the measured function.
    :return: The running time of f
    """
    start = time.time()
    f(arg for arg in args)
    return time.time() - start


if __name__ == "__main__":
    pass
