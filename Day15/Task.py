''' Task 1: Print Square Sequence using yield
            Create Generator method such that every time it will returns a next square number

            for exmaple : 1 4 9 16 ..
'''



def square_sequence():
    n = 1
    while True:
        yield n * n
        n += 1


# usage
sq = square_sequence()
print(next(sq), end=' ')
print(next(sq), end=' ')
print(next(sq), end=' ')
print(next(sq))
