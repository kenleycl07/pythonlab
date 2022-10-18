#########
### class
### Person
##########

# example 1
class Person:
    
    count_person = 0
    
    def __init__(self, name):
        self.name = name
        Person.count_person += 1
    
    def __str__(self):
        return f'{self.name}'
    
people = []
print(f"Number of  people in the population: {Person.count_person}")

p1 = Person('Bob Spone')
people.append(p1)
print(f"Number of  people in the population: {Person.count_person}")

p2 = Person('Nome Klone')
people.append(p2)
print(f"Number of  people in the population: {Person.count_person}")

p3 = Person('Dim Toman')
people.append(p3)
print(f"Number of  people in the population: {Person.count_person}")

p4 = Person('Gon Vinam')
people.append(p4)
print(f"Number of  people in the population: {Person.count_person}")

for person in people:
    print(person)

# example 2
class Person:
    count_person = 0

    def __init__(self, name):
        self.name = name
        Person.count_person += 1

    def __str__(self):
        return f'{self.name}'
    
    @classmethod
    def has_person(cls):
        if cls.count_person > 0:
            print('There is at least one person.')
        else:
            print('There is nobody there.')

Person.has_person()

p1 = Person('Bob Spone')
Person.has_person()

# example 3
class Person:
    firstname = " "
    lastname = " "
    age = " "
    tel = " "

    def get_input(self):
        self.firstname = input("Enter your firstname: ")
        self.lastname = input("Enter your lastname: ")
        self.age = input("Enter your age: ")
        self.tel = input("Enter your phone number: ")

    def display_output(self):
        f = open('people.txt', 'a')
        info_people = "{}, {}, {}, {}".format(self.firstname, self.lastname, self.age, self.tel)
        f.write(info_people)
        f.write('\n')
        f.close()

def main():
    people = []
    for i in range(0, 2):
        p = Person()
        p.get_input()
        people.append(p)

    for person in people:
        person.display_output()

if __name__ == '__main__':
    main()

# example 3
class Person:

    def get_input(self):
        self.firstname = input("Enter your firstname: ")
        self.lastname = input("Enter your lastname: ")
        self.age = input("Enter your age: ")
        self.tel = input("Enter your phone number: ")

    def display_output(self):
        f = open('people.txt', 'a')
        info_person = "Lastname: {}, Firstname: {}, Age: {} years old, Phone number: {}".format(self.lastname, self.firstname, self.age, self.tel)
        f.write(info_person)
        f.write('\n')
        f.close()

def main():          
    people = []
    for i in range(0, 2):
        p = Person()
        p.get_input()
        people.append(p)
    
    for pe in people:
        pe.display_output()
    

if __name__ == '__main__':
    main()

# example 4
def get_input():
    class Person:
        def __init__(self, firstname, lastname, age, tel):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.tel = tel

    people = list()
    for i in range(2):
        user_firstname = input("Enter your firstname: ")
        user_lastname = input("Enter your lastname: ")
        user_age = int(input("Enter your age: "))
        user_tel = input("Enter your phone number: ")
        p = Personne(user_firstname, user_lastname, user_age, user_age)
        people.append(p)
    return people


def display_output():
    record = get_input()
    for i in range(len(record)):
        data = f"{record[i].lastname} {record[i].firstname} {record[i].age} {record[i].tel}"
        f = open("people.txt", 'a', encoding="utf-8")
        f.write(data + "\n")
        f.close()

if __name__ == "__main__":
    display_output()
