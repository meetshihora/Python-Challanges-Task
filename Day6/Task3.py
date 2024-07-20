''' Task 3: Your monthly expense list (from Jan to May) looks like this,
        expense_list = [2340, 2500, 2100, 3100, 2980]
        Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well. '''

# Solution
expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter an expense amount: "))
for i in range(0,5):
    if expense_list[i] == expense:
        print("Expense is found in month",i+1)
        break
else:
    print("Expense is not found")

# Output
'''
Enter an expense amount: 2500
Expense is found in month 2
'''