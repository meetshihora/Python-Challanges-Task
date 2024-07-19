# Task 1: Using following list of cities per country,
#         india = ["mumbai", "banglore", "chennai", "delhi"]
#         pakistan = ["lahore","karachi","islamabad"]
#         bangladesh = ["dhaka", "khulna", "rangpur"]

#         1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
#         2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# 1 SOLUTION
city = input("Enter a city name: ")

if city in india:
    print("City belongs to India")
elif city in pakistan:
    print("City belongs to Pakistan")
elif city in bangladesh:
    print("City belongs to Bangladesh")
else:
    print("City doesn't belong to any country")

#Output:

# Enter a city name: mumbai
# City belongs to India

# 2 SOLUTION
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