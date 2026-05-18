# OOP


class Car():
    wheel = 4
    color = "green"
    brand = "BMW"
    

obj = Car()
print(obj.wheel)

class Car():
    wheel = 4
    color = "green"
    brand = "Tesla"
    
    def info(self):
        return f'car brand name is {self.brand}'
    
    def car_info2(self):
        info = self.info()
        return f'wheel {self.wheel} {info}'
        
obj = Car()
print(obj.wheel)
print(obj.car_info2())
obj.c = 100 # obj attrs
print(obj.c)

print("---------------------")

class Test():
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(a,b,c)
        print("The value of a is", a)
        print("I am here.")
    
    def __str__(self):
        return f'This is class object, {self.a}'
    
    def add(self, data):
        self.data = data
        return self.a + self.b + data
    
    def result(self):
        return self.data
    
obj = Test(11,20,4)
print(obj.add(600))
print(obj.result())
