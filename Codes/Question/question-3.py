class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def is_valid_id(self):
        return len(self.student_id) == 8

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"


# Get the number of students from input
num_students = int(input("Enter number of students: "))

students = []

# Get the details of each student
for _ in range(num_students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    student = Student(student_id, name)
    students.append(student)

# Print the details of the students
for student in students:
    if student.is_valid_id():
        print(student)
    else:
        print(f"Invalid ID for {student.name}")
