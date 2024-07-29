# Task 2: Use del property to first delete id attribute and then the entire object

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

emp = Employee(1, "coder")

del emp.id
try:
    print(emp.id)
except AttributeError:
    print("id attribute deleted")

del emp
try:
    print(emp)
except NameError:
    print("emp object deleted")