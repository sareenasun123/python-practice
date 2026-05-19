a = [1,2,3,4]
a[0] = 2
print(a)

# Tuple

print("-------------Tuple-------------")
# Tuple value cannot be changed.
# Tuples are ordered collections.
b = (1,2,4,5)
# b[0] = 2
print(b)
print(type(b))
for i in b:
    print(i)
    
# set
# set does not support duplicate data
# set are unordered collections.
# We cannot access values or data from set using index. 
print("-------------SET-------------")
a = {"test","hello",1,2,"namaste",1,1,1,1}
print(type(a))
print(a)

a = [1,2,3,4,1,1,1,1]
b = set(a)
print(b)
a.remove(1)
print(a)


print("-------------FUNCTION-------------")

# We don't use print() inside function.
def test():
    # print("I am inside function.")
    a = 1
    if a == 2:
        return 2
    else:
        return a,a

data = test()    
print(data)

def total():
    a = [56,232,23,23,2,32,32]
    sum = 0
    for i in a:
        sum += i
    return sum
    
data = total()
print(data)