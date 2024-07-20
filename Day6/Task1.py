'''Task 1:After flipping a coin 10 times you got this result,
        result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
        Using for loop figure out how many times you got heads '''

# Solution
import random
result = [] 
j = 0
for i in range(10):
    result.append(random.choice(["heads","tails"]))
    if result[i] == "heads":
        j= j+1

print(result)
print('how many times you got heads',j)

# Output
'''
['heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads']
how many times you got heads 10
'''