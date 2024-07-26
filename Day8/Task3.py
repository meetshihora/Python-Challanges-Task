''' Task 3: Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them.'''

# Solution

def circle_calc(radius):
    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    diameter = 2 * radius
    return area, circumference, diameter

radius = float(input("Enter radius of circle: "))
area, circumference, diameter = circle_calc(radius)
print(f"Area: {area}, Circumference: {circumference}, Diameter: {diameter}")
