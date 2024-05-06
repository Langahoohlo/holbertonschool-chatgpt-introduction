#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the factorial of the number provided as a command line argument
f = factorial(int(sys.argv[1]))
print(f)

