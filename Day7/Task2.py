''' Task 2: Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
            rectangle area=length*width
        If no shape is supplied then it should take triangle as a default shape '''

# Solution

def calculate_area(base,height,shape="triangle"):
    if shape == "triangle":
        area = (1/2)*base*height
    elif shape == "rectangle":
        area = base*height
    else:
        raise "Invalid shape type. Please provide either 'triangle' or 'rectangle'."
    return area

print(calculate_area(3,4))


# Output

# 6.0
