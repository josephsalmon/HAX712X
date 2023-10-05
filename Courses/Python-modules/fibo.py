# Fibonacci numbers module


def fib_print(n):
    """
    Print Fibonacci sequence up to n.

    Parameters:
        n (int): A decimal integer


    """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib_list(n):
    """
    Compute Fibonacci sequence up to n.

    Parameters:
        n (int): A decimal integer

    Returns:
        result (list): A list containing the Fibonacci numbers up to n

    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
