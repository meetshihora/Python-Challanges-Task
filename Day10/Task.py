''' Task 1: Create a sample class named Employee with two attributes id and name
        employee :
        id
        name

        object initializes id and name dynamically for every Employee object created.
        emp = Employee(1, "coder") '''

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


emp = Employee(1, "coder")

print(emp.id)
print(emp.name)
print(emp.__dict__)