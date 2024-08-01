''' Task 1: Create multiple inheritance on teacher,student and youtuber.
            Q. if we have created teacher and now one student joins master degree with becoming teacher then what?
            Ans :  just make subclass from  teacher so that student will become teacher ''' 

class Teacher:
    def teach(self):
        print("Teacher Teaching")

class Student:
    def study(self):
        print("Student Studying")

class Youtuber:
    def upload(self):
        print("Youtuber Uploading")

class MasterDegreeTeacher(Teacher,Student):
    def __init__(self,name,age):
        self.name=name
        self.age=age

print("Task 1: ",end="")
obj=MasterDegreeTeacher("John",25)
obj.teach()
obj.study()
