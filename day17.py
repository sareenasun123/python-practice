# data access modifier

'''
public 

private
'''


# class Test():
#     a = 10
#     __b = 100
    
#     def __display(self):
#         return self.__b
    
    
#     def add(self):
#         return self.a+self.__b
    
    
    
# obj = Test()
# print(obj.a)
# print(obj.add())



    
# class Person():
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.age_pub = self.__age -1

#     def displayPerson(self):
#         return f'{self.__name},{self.__age}'

# class Worker():
#     def __init__(self, company,salary):
#         self.company =company
#         self.salary = salary


#     def displayworker(self):
#         return f'{self.company},{self.salary}'



# class Engineer(Person,Worker):
#     def __init__(self, name, age, company, salary):
#         Person.__init__(self,name, age)
#         Worker.__init__(self,company,salary)

#     def displayengineer(self):
#         print(self.age_pub)
#         return f'{self.displayPerson()}, {self.displayworker()}'

# print(Engineer.__mro__)

# obj= Engineer("shashi",22,'aura',90000)
# print(obj.displayengineer())



'''
Create a class BankAccount with:

private variables: accountNumber, balance
public methods: deposit(amount), withdraw(amount), displayBalance()

Create a subclass SavingsAccount that inherits BankAccount.
public attrs: rate, time
Add a method addInterest()

'''

print("------------------BANK_ACCOUNT------------------")


class BankAccount():
    __accountNumber = "1234567890"
    __balance = 1000
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance
        
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        return self.__balance
        
    def displayBalance(self, ):
        return self.__balance
        
        
class SavingAccount(BankAccount):
    rate = 50
    time = 1
    
    def addInterest(self):
        print("Do add interest here.")
        
    def addInterest(self):
        balance = self.displayBalance()
        interest = (balance * self.rate * self.time) / 100
        self.deposit(interest)
        return balance
        

obj = SavingAccount()
print(obj.deposit(500))
print(obj.displayBalance())  # 1500
print(obj.addInterest())
print(obj.displayBalance())  # 2250
        

class Parent1():
    
    def display(self):
        return ("This is higher parent 1.")

class Parent2():
    
    def display(self):
        return ("This is lower parent 2.")
    
obj = Parent1()
obj1 = Parent2()


for i in (obj, obj1):
    print(i.display())
    
