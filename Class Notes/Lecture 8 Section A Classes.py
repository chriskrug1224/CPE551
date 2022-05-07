#Lecture 8 Section A Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def compute_salary(self):
        return 60000
    def number_of_vacation(self):
        return 20

class Engineer(Employee):
    def compute_salary(self):
        return 100000

class Manager(Employee):
    def set_works(self, people):
        self.workers = people

    def compute_salary(self):
        return 90000

    def number_of_vacation(self):
        return 25
        
class Other(Employee):
    pass

#one_person = Person("Sue", 25)
#print(one_person.name, one_person.age)
one_engineer = Engineer("Sue", 25)
print(one_engineer.name, one_engineer.age)
print("Salary = ", one_engineer.compute_salary())
print("Vacation = ", one_engineer.number_of_vacation())
