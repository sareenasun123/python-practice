# Function with keyword arbitrary argument
def data(**kwargs):
    print(type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    

    if "lname" in kwargs.keys():
        print("Last name: ", kwargs['lname'])
    else:
        print("Last name is missing.")


data(fname="sam", lname="rai",age=13, num=12345, address= "")
data(fname="samriddhi", num=12543, address= "")



print("------------------Using get()------------------")

def data(**kwargs):
    print(type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    
    age = kwargs.get('age')
    print(age)
    if age is None:
        print("age key is missing.")
    else:
        print(age)

data(fname="sam", lname="rai",age=13, num=12345, address= "")

print("------------------MARKSHEET------------------")

def marks_sheet(*args, **kwargs):
    avg = sum(args)/len(args)
    max_num = max(args)
    min_num = min(args)
    max_number = args[0]
    min_number = args[0]
    for i in args:
        if i>max_number:
            max_number = i
        else:
            min_number = i
    
    # print(avg)
    # print(args)
    # print(kwargs)
    return f'{kwargs.get('name')} obtained {avg}% \nMaximum number is {max_num} and minimum number is {min_num}.'

print(marks_sheet(100,78,67,89,78, name="Sam", grade=10))
print(marks_sheet(100,89,78, name="Ava", grade=10))