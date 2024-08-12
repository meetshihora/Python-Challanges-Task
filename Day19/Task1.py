# Task 1: Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

def check_non_negative_integer(func):
    def wrapper(n):
        if isinstance(n, int) and n >= 0:
            return func(n)
        else:
            raise ValueError("Argument must be a non-negative integer")
    return wrapper

@check_non_negative_integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(5))  
    print(factorial(-3))
except ValueError as e:
    print(e)

