#  Task 2: Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range  is 80 to 100
#         1. Ask user to enter his fasting sugar level
#         2. If it is below 80 to 100 range then print that sugar is low
#         3. If it is above 100 then print that it is high otherwise print that it is normal

# Solution 1

sugar = int(input("Enter your fasting sugar level: "))

if sugar < 80:
    print("Sugar is low")
elif sugar > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")

# Output

# Enter your fasting sugar level: 90
# Sugar is normal