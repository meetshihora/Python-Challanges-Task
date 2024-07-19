''' Task 1: Using following list of cities per country,
         india = ["mumbai", "banglore", "chennai", "delhi"]
         pakistan = ["lahore","karachi","islamabad"]
         bangladesh = ["dhaka", "khulna", "rangpur"]

    2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country" '''


# SOLUTION
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")   

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")

# Output:

# Enter first city: mumbai
# Enter second city: karachi
# They don't belong to same country