class Course:
    def __init__(CourseType):
        print('Course is a ', CourseType)

class Student(Course):
    def __init__(self):
        Course.__init__('Student')

print(issubclass(Student, Course))
print(issubclass(Student, list))
print(issubclass(Student, (list, Course)))
print(issubclass(Student, (list, Course)))