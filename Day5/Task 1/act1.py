'''Task 1: Using following list of cities per country,
#         india = ["mumbai", "banglore", "chennai", "delhi"]
#         pakistan = ["lahore","karachi","islamabad"]
#         bangladesh = ["dhaka", "khulna", "rangpur"]

# 1. Write a program that asks user to enter a city name and it should tell which country the city belongs to '''

# Solution:
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

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

