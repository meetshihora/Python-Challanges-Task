''' Task 2: Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
        a + i = 0

            Example:

                integer = [1, -1, 2, 3, 5, 0, -7]
                additive_inverse = [-1, 1, -2, -3, -5, 0, 7] '''


integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [i if i == 0 else -i for i in integer]
print(additive_inverse)
