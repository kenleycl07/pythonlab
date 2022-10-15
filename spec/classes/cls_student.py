#################
### class
### Student
#################

class Student:
    name = " "
    enroll = " "

    def setStudent(self):
        self.name = input("Enter your name: ")
        self.enroll = input("Enter your enrollment: ")

    def showStudent(self):
        print("Name: ", self.name)
        print("Enrollment: ", self.enroll)

students = []
n = int(input('Enter number of students: '))
for i in range(0, n):
    s = Student()
    s.setStudent()
    students.append(s)

for std in students:
    std.showStudent()


# example
class Student:
    
    def __init__(self, firstname, lastname, dob, field):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.field = field
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Courses:
    
    def __init__(self, number, name, max_std):
        self.number = number
        self.name = name
        self.max_std = max_std
        self.students = []
        
    def registerStudent(self, student):
        if len(self.students) < self.max_std:
            self.students.append(student)
            return True
        return False

# students
std1 = Student('Bob', 'Spone', 'december 1999', 'Mathematics')
std2 = Student('Nome', 'Klone', 'october 1998', 'Computer Science')
std3 = Student('Dim', 'Toman', 'june 2000', 'Computer Science')
std4 = Student('Gon', 'Vinam', 'january 2000', 'Mathematics')
std5 = Student('Clar', 'Ching', 'november 1999', 'Computer Science')
std6 = Student('San', 'Lonem', 'april 1998', 'Psychology')

# courses
calculus = Courses('002', 'Calculus', 3)
chemistry =  Courses('003', 'Basic chemistry', 3)
physics =  Courses('004', 'Introduction to Physics', 3)
biology = Courses('005', 'Introduction to Biology', 3)

# add students to chemistry class
if chemistry.registerStudent(std1):
    print(f'{std1} registered !')
else:
    print(f'Sorry, {std1} cannot register in this course.')
    
if chemistry.registerStudent(std2):
    print(f'{std2} registered !')
else:
    print(f'Sorry, {std3} cannot register in this course.')

if chemistry.registerStudent(std3):
    print(f'{std3} registered !')
else:
    print(f'Sorry, {std4} cannot register in this course.')
    
if chemistry.registerStudent(std4):
    print(f'{std4} registered !')
else:
    print(f'Sorry, {std4} cannot register in this course.')

