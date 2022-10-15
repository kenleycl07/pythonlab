#################
### class
### Person
### Student
#################

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return "I am {} {} and I am {} years old.".format(self.firstname, self.lastname, self.age)

class Student(Person):
    def __init__(self, firstname, lastname, age, nb_credits):
        super().__init__(firstname, lastname, age)
        self.nb_credits = nb_credits

    def __str__(self):
        return "I am {} {}, I am {} years old. And I have {} credits".format(self.firstname, self.lastname, self.age, self.nb_credits)

# create a Person object
p1 = Person('Bob', 'Sponge', 20)
# create a Student object
et1 = Student('Bobby', 'Spongy', 21, 110)
# create a Student object as a Person object
et2 = Person('Bobino', 'Spongino', 20)
print(p1)
print(et1)
print(et2)


# example
class Person:
    
    def __init__(self, firstname, lastname, dob):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
    
    def __str__(self):
        return f'{self.firstname}, {self.lastname}'
    
class Student(Person):
    
    def __init__(self, firstname, lastname, dob, field):
        super().__init__(firstname, lastname, dob)
        self.field = field
    
std1 = Student('Bob', 'Spone', 'december 1999', 'Mathematics')
std2 = Student('Nome', 'Klone', 'october 1998', 'Computer Science')

print(std1, std1.field)
print(std2, std2.field)

















