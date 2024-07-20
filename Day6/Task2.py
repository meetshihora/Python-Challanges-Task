''' Task 2: Print square of all numbers between 1 to 10 except even numbers '''

# Solution
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

# Output
'''
1
9
25
49
81
'''