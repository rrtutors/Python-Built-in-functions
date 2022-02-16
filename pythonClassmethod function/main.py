class Student:
    course = "Computer Science"
    def printCourse(a):
        print('My Course is:', a.course)

Student.printCourse = classmethod(Student.printCourse)

Student.printCourse()

