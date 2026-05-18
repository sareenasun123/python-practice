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
        super().__init()
        # print("This is from parent class."super().b)
    
    a = 2
    c = 1000
    d = "Sam"
    
    
obj = Child()
print(obj.a) # There are two same variables but since the object is made of child class, it takes the value of the child class first.
print(obj.add())