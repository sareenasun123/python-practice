class Parent():
    a = 10
    b = 11
    
    def __init__self():
        print("I am from parent class.")
    
    def add(self):
        return self.a + self.b
    
     
class Child(Parent):
    
    def __init__(self):
        print("I am from parent class.")
        # Parent.__init__(self)
        super().__init__()
        self.aa = super().a
        # print("This is from parent class."super().b)
    
    a = 2
    c = 1000
    d = "Sam"

class Child1(Child):
    d = 2
    a = 200
    
    def value_a(self):
        return super().a, self.aa, self.a
           
    
obj = Child1()
print(obj.a) # There are two same variables but since the object is made of child class, it takes the value of the child class first.
# print(obj.add())
print(obj.value_a())



class Parent2():
    c = 100
    d = 50
    def parent_method(self):
        return "from parent2 class"
    
    
    
class Parent1():
    a = 20
    b = 30
    def parent_method(self):
        return "from parent1 class"
    
class Child(Parent1, Parent2):
    e = 1
    f = 2
    def parent_method(self):
        return f'{super().parent_method()}, {Parent1.parent_method(self)}'    
    
print(Child.__mro__)

obj = Child()
print(obj.a)


print("--------------ASSIGNMENT--------------")

# Without constructor
'''
class Person:
    name = "Sam"
    age = 17

    def displayPerson(self):
        return f'Person name is {self.name} and age is {self.age}'
    
class Worker:
    company = "Microsoft"
    salary = 200000
    
    def displayWorker(self):
        return f'Company name is {self.company} and salary is {self.salary}.'
    
class Engineer(Person, Worker):
    def displayEngineer(self):
        return f"Engineer"
    
obj = Engineer()
print(obj.displayPerson())
print(obj.displayWorker())
print(obj.displayEngineer())
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayPerson(self):
        return f'Person name is {self.name} and age is {self.age}'
    
class Worker:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary
    
    def displayWorker(self):
        return f'Company name is {self.company} and salary is {self.salary}.'
    
class Engineer(Person, Worker):
    def __init__(self, name, age, company, salary):
        Person.__init__(self,name,age)
        Worker.__init__(self,name,age)
    def displayEngineer(self):
        return f"Engineer"
    
obj = Engineer("Sam", 17, "Microsoft", 200000)
print(obj.displayPerson())
print(obj.displayWorker())
print(obj.displayEngineer())