if (1==1):
    print("This is true.")
else:
    if (2==2):
        print("These 2 are equal.")
    print("This is false.")


age = 21
country = "Nepal"

if age > 18:
    if country == "Nepal":
        print("Eligible for license")
    elif country == "India":
        print("Special license for SAARC country")
    else:
        print("Not eligible for license")
else:
    print("Under age")



gender = "F"
if gender == "M":
    print("Male")
else:
    print("Female")



data = "Male" if gender == "M" else "Female"
print(data)


print("----------------------"*2)

a = [1,2,3,4,5,6]
print(a)
print(type(a))
print(a[0])
print(a[-1])


print(len(a))
# -8 to 7


print(a[0:4])
print(a[1:])
print(a[:6])
print(a[:])




data = [1, "Test",4.5,None,1]
print(data)
print(data[1])
print(isinstance(data[1],str))


# print(type(data[1])==str)

data = [1, "Test",4.5,None,1]
data[0] = "This is updated on"
# data[5] = "zero"
print(data)



'''
append
insert
extend
concat
'''

# append => adds an element to the end of a list  
data = ["hello", "test", 1, 2, 3, 4, "broadway"]
data.append(1.6)  # append()
data.append("added")
print(data)

# insert 
data = ["hello","test",1,2,3,4,"broadway"]
data.insert(1000,"sam")
print(data)


# extends
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
print(b)

# concat

a = [1,2,3]
b = [4,5,6]
c = b+a
print(c)
print(a)
print(b)

