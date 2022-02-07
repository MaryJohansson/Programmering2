class Student:

    def __init__(self, ssn, name, age, classroom, school):
        self.ssn = ssn
        self.name = name
        self.age = age
        self.classroom = classroom
        self.school = school
        pass

    def __eq__(self, other):
        return self.ssn == other

    def change_school(self):
        pass