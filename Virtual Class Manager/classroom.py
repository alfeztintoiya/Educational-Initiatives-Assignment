from student import Student
from assignment import Assignment

class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = {}
        self.assignments = []
        self.attendance_log = {}
    
    def add_student(self,student_id):
        if student_id in self.students:
            raise ValueError(f"Student {student_id} already in {self.name}")
        self.students[student_id] = Student(student_id)
    
    def schedule_assignment(self,detail):
        assignment = Assignment(detail)
        self.assignments.append(assignment)
    
    def get_assignment(self,detail):
        for assignment in self.assignments:
            if assignment.detail == detail:
                return assignment
        return None

    def mark_attendance(self,session_name,student_id):
        if student_id not in self.students:
            raise ValueError(f"Student {student_id} not in {self.name}")
        student = self.students[student_id]
        student.mark_attendance(session_name)
        self.attendance_log.setdefault(session_name,[]).append(student_id)