a = [1,2,3,4,5,6,7,8,0]
# in, not in 
print(10 in a)

# for loop syntax

# for i in <sequence_data>:
#   <code block>
# for i in [1,2,3,4,5,6,7,8]:
#     print(i)

# a = "broadway"
# print("This is string index 0", a[0])

# for i in a:
#     print(i)

data = {
    "name": "Ayusha",
    "address": "Banepa",
    "age": 22,
    "phone": 9812345678,   
}

for i in data:
    print(f'{i} = {data[i]}')

print(data.items())
for key, value in data.items():
    print(key, value)

for index, data in enumerate(items):
    print(index+1, data)

for i in range(1,20,1):
    print(i)
for i in range(20,1,-1):
    print(i)
    