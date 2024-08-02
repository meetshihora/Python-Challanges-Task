''' Day 13: Raise Exception And Finally

    Task 1: Create a custom exception AdultException.

    Task 2: Create a class Person with attributes name and age in it.
    
    Task 3: Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.

    Task 4: Create a function display_person() which prints the age and name of a person.
        let us say,

        if age>18 
            he is major
        else
            raise exception

        create cusomException named ismajor and raise it if age<18. '''


# task 1
class AdultException(Exception):
    pass

# task 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# task 3
    def get_minor_age(self):
        if self.age > 18:
            return self.age
        else:
            raise AdultException("{} is minor".format(self.name))

# task 4
def display_person(person):
    try:
        age = person.get_minor_age()
        print("{} is {} years old and he is major".format(person.name, age))
    except AdultException as e:
        print(str(e))


