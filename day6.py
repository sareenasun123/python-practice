# del
# remove
# pop
# clear

a = [1, 2, 3, 4, 5]
del a[3]
print(a)

a = [1, 2, 3, 4, 5, 1, 1]
a.remove(2)
a.remove(1)

print(a)

a = [1, 2, 3, 4, 5, 1, "testing"]
result = a.pop(0)
a.pop()
print(a)
print(result)

# clear
a = [1, 2, 3, 4, 5, 1, "testing"]
a.clear()
print(a)

'''
sort()
reverse()
count()
'''
print("SORT, REVERSE AND COUNT")

a = [1,32,13,1,4,55,65,61]
a.sort()
print(a)

a = [1,32,13,1,4,55,65,61]
a.sort(reverse=True)
print(a)

a = [1,32,13,1,4,55,65,61]
a.reverse()
print(a)

print(a.count(32))

a = [1,2,3,4,[6,7,8]]
print(a[4][1])

'''
Enter 5 inputs for user all in int
add 5 input data in list
find the average of all items number

'''
a = int(input("Enter a number: "))
print(type(a))
print("Enter value of a is", a)

# result = ['a','b','c','d','e']

a = int(input("Enter a number, a: "))
b = int(input("Enter a number, b: "))
c = int(input("Enter a number, c: "))
d = int(input("Enter a number, d: "))
e = int(input("Enter a number, e: "))

result = []
result.append(a)
result.append(b)
result.append(c)
result.append(d)
result.append(e)

print(result)
avg = (result[0]+result[1])/len(result)
print(avg)
