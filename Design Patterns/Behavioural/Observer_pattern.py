class Student:
    def __init__(self,name):
        self.name = name
    
    def update(self,message):
        print(f"{self.name} received notification: {message}")

class Teacher:
    def __init__(self):
        self.students = []
    
    def attach(self,student):
        self.students.append(student)
    
    def detach(self,student):
        self.students.remove(student)
    
    def post_announcement(self,message):
        print(f"\nTeacher posts: {message}")
        for student in self.students:
            student.update(message)

s1 = Student("Alfez")
s2 = Student("Yash")

teacher = Teacher()
teacher.attach(s1)
teacher.attach(s2)
teacher.post_announcement("Exam on Friday!")