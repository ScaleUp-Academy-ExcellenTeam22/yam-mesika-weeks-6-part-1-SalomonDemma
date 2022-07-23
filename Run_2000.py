import time


def timer(function: callable, *args) -> float:
    """
    A function that receives a function and other parameters.
    The function measure how long the function received ran when the same
    parameters are passed to it.
    :param function: A function that will measure its running time.
    :param args: Parameters for the measured function.
    :return: The running time of function
    """
    start_time = time.time()
    function(*args)
    return time.time() - start_time


if __name__ == "__main__":
    print(timer(sum, list(range(10**6))))
