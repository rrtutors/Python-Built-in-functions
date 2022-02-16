class Student(object):
    def __init__(self, college):
        print('Name of the College:', college)

class Computer_science(Student):
    def __init__(self):
        # call superclass
        super().__init__('University of Hull')
        print('University of Hull offers Computer Science')

student = Computer_science()
