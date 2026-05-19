def add(a, b):
    return a+b


print(add(10,50))
print(add(100,200))
print(add(1,9))



def user_info(fname, lname):
    return f'First name is {fname} and last name is {lname}'

print(user_info("Anu", "Rai"))


# default args
# Positional argument must be written at first.
# We should write default argument at the end.
def area(r, pi=3.14, data = 1):
    area_of_circle = pi * r ** 2
    return area_of_circle



print(area(7))
print(area(2,3.9))


def user_info(fname, lname, age):
    return f'First name is {fname}, last name is {lname} and age is {age}.'


print(user_info(lname="Rai",fname = "Sam", age = 16))




print("-------------Bill-------------")

def calculate_bill(item, item_price, quantity, tax_rate=0.13, discount=0):
    total = item_price * quantity
    total = total + (total * tax_rate) - (total * discount)
    return total
    
print(calculate_bill("mac",11500,3, tax_rate=0.13, discount=0.2))
print(calculate_bill("iPhone",125000,2, tax_rate=0.13, discount=0.2))
print(calculate_bill("PC",250000,1, tax_rate=0.13, discount=0.2))
print(calculate_bill("iPad",100000,2, tax_rate=0.13, discount=0.2))
print(calculate_bill("airpod",12000,4, tax_rate=0.13, discount=0.2))
print(calculate_bill("apple watch",20000,3, tax_rate=0.13, discount=0.2))



def add(*data):
    print(data)
    return data


add(1,2)
add(1,2,3)
add(1)