# Task 1: Let us say your expense for every month are listed below,
#         January - 2200
#         February - 2350
#         March - 2600
#         April - 2130
#         May - 2190

#         Create a list to store these monthly expenses and using that find out,
#             1. In Feb, how many dollars you spent extra compare to January?
#             2. Find out your total expense in first quarter (first three months) of the year.
#             3. Find out if you spent exactly 2000 dollars in any month
#             4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#             5. You returned an item that you bought in a month of April and 
#             got a refund of 200$. Make a correction to your monthly expense list based on this

# Solution:

expenses = [2200, 2350, 2600, 2130, 2190]

print("In Feb, how many dollars you spent extra compare to January?", expenses[1] - expenses[0])

print("Find out your total expense in first quarter (first three months) of the year.", sum(expenses[0:3]))

print("Find out if you spent exactly 2000 dollars in any month.", 2000 in expenses)

expenses.append(1980)
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list", expenses)

expenses[3] = expenses[3] - 200
print("You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this", expenses)

# Output:

# In Feb, how many dollars you spent extra compare to January? 150
# Find out your total expense in first quarter (first three months) of the year. 7150
# Find out if you spent exactly 2000 dollars in any month. False
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list [2200, 2350, 2600, 2130, 2190, 1980]
# You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this [2200, 2350, 2600, 1930, 2190, 1980]
