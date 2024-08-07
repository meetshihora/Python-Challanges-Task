''' Task 3: Create a set which only contains unique sqaures from a given a integer list.
        integer = [1, -1, 2, -2, 3, -3]
        sq_set = {1, 4, 9} '''


integer = [1, -1, 2, -2, 3, -3]
sq_set = {num**2 for num in integer}
print(sq_set)
