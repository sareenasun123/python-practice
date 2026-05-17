# dictionary
data = {
    "name": "Ayusha",
    "address": "Banepa",
    "age": 22,
    "percentage": 81.25,
    "phone": 9812345678,
    
}
print(type(data))
print(data)
print(len(data))


print(data['name'])
print(data.keys())
print(data.values())

data = {
    "name": "Ayusha",
    "address": "Banepa",
    "age": 22,
    "percentage": 81.25,
    "phone": 9812345678,   
}

data["age"] = 45   # in dictionary, the value can be changed but keys cannot be changed.
data["percentage"] = 90.15
data["temp_num"] = 98012

print(data)

# update
data.update({
    "age": 45,
    "percentage": 100,
    "temp_num": 98012
})
print(data)

'''
del => It deletes references to objects.
    => It removes a variable, elemnts at a specific index or via slicing and permanently deletes a key-value pair from a dictionary. 
pop => removes and returns an item from a collection.
popitem => It removes and returns the last key-value pair from a dictionary
clear => It remove all elements from a mutable collection such as a list, dictionary or set.

'''

data = {
    "name": "Ayusha",
    "address": "Banepa",
    "age": 22,
    "percentage": 81.25,
    "phone": 9812345678,
    "temp_num": 98012,
}


del data['age']
print(data)

name = data.pop("name")
print(name)

data.popitem()
# data = {}
# data.popitem()

print(data)
data.clear()
print(data)

data = {
    "name": "Ayusha",
    "address": "Banepa",
    "age": 22,
    "phone" : [
        {"type": "ncl", "num" : 9812345678},
        {"type": "ntc", "num" : 9862387654},
    ],
    "percentage": 81.25,
    "temp_num": {"type": "ntc", "num": 9862387654},
}

# print(data['name'])
print(data.get('names'))  # get() returns none if there is no value.
print(data["phone"][0]["type"])

'''
Ayusha ntc number is 9812345678
Ayusha ncl number is 9812345678

'''

print(f"{data['name']} {data['phone'][0]['type']} number is {data['phone'][1]['num']}")

