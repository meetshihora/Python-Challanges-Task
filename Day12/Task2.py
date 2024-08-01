''' Task 2: Now student is teacher as well as youtuber then what???
            -just use multiple inheritance for these three relations '''

class Student:
    def study(self):
        print("Student Studying")

class Teacher:
    def teach(self):
        print("Teacher Teaching")

class Youtuber:
    def upload(self):
        print("Youtuber Uploading")

class StudentTeacherYoutuber(Student,Teacher,Youtuber):
    pass

obj=StudentTeacherYoutuber()
obj.teach()
obj.study()
obj.upload()