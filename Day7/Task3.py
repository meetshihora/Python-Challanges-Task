''' Task 3: Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
        *
        **
        ***
        if input is 4 then it should print
            *
            **
            ***
            ****
    Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)'''


# Solution

def print_pattern(number):
    for i in range(number):
        for j in range(i+1):
            print("*", end="")
        print()

number = int(input("Enter the number: "))
print_pattern(number)