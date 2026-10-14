class Student:
    def __init__(self, grade):
        self.__grade = grade

    def study(self):
        print("Student is studying.")


class CollegeStudent(Student):
    def study(self):
        print("College student is studying programming.")


student = Student("A")
college_student = CollegeStudent("A")

student.study()
college_student.study()