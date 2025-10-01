class Student:
    def __init__(self,student_id):
        self.student_id = student_id
        self.submissions = []
        self.attendance = []
    
    def submit_assignment(self,assignment_detail):
        self.submissions.append(assignment_detail)

    def mark_attendance(self,session_name):
        self.attendance.append(session_name)