''' Task 3: Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

        example: 

            factorial(1.354) : raise Exception or print error message
            factorial(-1) : raise Exception or print error message
            factorial(5) : 60
'''

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
    print(factorial(1.354))  
except ValueError as e:
    print(e)

try:
    print(factorial(-1))  
except ValueError as e:
    print(e)

try:
    print(factorial(5))  
except ValueError as e:
    print(e)
