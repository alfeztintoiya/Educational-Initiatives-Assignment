from classroom import Classroom
from logger_config import setup_logger

logger = setup_logger()

class VirtualClassManager:
    def __init__(self):
        self.classrooms = {}
    
    def _get_classroom(self,class_name):
        if class_name not in self.classrooms:
            raise ValueError(f"Classroom {class_name} does not exist.")
        return self.classrooms[class_name]
    
    def add_classroom(self,name):
        if name in self.classrooms:
            raise ValueError(f"Classroom {name} already exists.")
        self.classrooms[name] = Classroom(name)
        logger.info(f"Classroom {name} has been created.")
    
    def add_student(self,student_id,class_name):
        classroom = self._get_classroom(class_name)
        classroom.add_student(student_id)
        logger.info(f"Student {student_id} has been enrolled in {class_name}")

    def schedule_assignment(self,class_name,detail):
        classroom = self._get_classroom(class_name)
        classroom.schedule_assignment(detail)
        logger.info(f"Assignment for {class_name} has been scheduled.")
    
    def submit_assignment(self,student_id,class_name,detail):
        classroom = self._get_classroom(class_name)
        if student_id not in classroom.students:
            raise ValueError(f"Student {student_id} not enrolled in {class_name}")
        
        assignment = classroom.get_assignment(detail)
        if not assignment:
            raise ValueError(f"Assignment: '{detail}' not found in {class_name}")

        student = classroom.students[student_id]
        student.submit_assignment(detail)
        assignment.submitted_by.add(student_id)
        logger.info(f"Assignment submitted by student {student_id} in {class_name}")
    
    def mark_attendance(self,class_name,session_name,student_id):
        classroom = self._get_classroom(class_name)
        classroom.mark_attendance(session_name,student_id)
        logger.info(f"Attendance marked for student {student_id} in {class_name} ({session_name}).")
    
    def list_classrooms(self):
        return list(self.classrooms.keys())

    def list_students(self,class_name):
        classroom = self._get_classroom(class_name)
        return list(classroom.students.keys())
    
    def list_attendance(self,class_name,session_name):
        classroom = self._get_classroom(class_name)
        return classroom.attendance_log.get(session_name,[])
    

    def handle_command(self,command):
        try:
            parts = command.split()
            cmd = parts[0]

            if cmd=="add_classroom":
                self.add_classroom(parts[1])
            elif cmd=="add_student":
                self.add_student(parts[1],parts[2])
            elif cmd=="schedule_assignment":
                class_name = parts[1]
                detail = " ".join(parts[2:])
                self.schedule_assignment(class_name,detail)
            elif cmd=="submit_assignment":
                student_id = parts[1]
                class_name = parts[2]
                detail = " ".join(parts[3:])
                self.submit_assignment(student_id,class_name,detail)
            elif cmd=="mark_attendance":
                class_name = parts[1]
                session_name = parts[2]
                student_id = parts[3] 
                self.mark_attendance(class_name,session_name,student_id)
            elif cmd=="list_classrooms":
                logger.info(f"Classrooms: {self.list_classrooms()}")
            elif cmd=="list_students":
                class_name = parts[1]
                logger.info(f"Students in {class_name}: {self.list_students(class_name)}")
            elif cmd=="list_attendance":
                class_name = parts[1]
                session_name = parts[2]
                logger.info(f"Attendance for {class_name}, session {session_name}: {self.list_attendance(class_name,session_name)}")
            elif cmd=="exit":
                logger.info("Existing Virtual Classroom Manager.")
                return False
            else:
                logger.warning("Invalid Command.")
        except Exception as e:
            logger.error(e)

        return True

    def show_commands(self):
        commands_info = [
            ("add_classroom <class_name>", "Create a new classroom"),
            ("add_student <student_id> <class_name>", "Enroll a student in a classroom"),
            ("schedule_assignment <class_name> <assignment_detail>", "Schedule an assignment for a class"),
            ("submit_assignment <student_id> <class_name> <assignment_detail>", "Submit an assignment for a student"),
            ("mark_attendance <class_name> <session_name> <student_id>", "Mark attendance for a student"),
            ("list_classrooms", "List all classrooms"),
            ("list_students <class_name>", "List all students in a classroom"),
            ("list_attendance <class_name> <session_name>", "List students present in a session"),
            ("exit", "Exit the Virtual Classroom Manager")
        ]

        max_len = max(len(cmd) for cmd, _ in commands_info)

        print("\nAvailable Commands:\n")
        for cmd, desc in commands_info:
            print(f"{cmd.ljust(max_len)}  -> {desc}")
        print("\n")
