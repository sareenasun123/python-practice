# Exception

try:
    print(1+"a")
except:
    print("something went wrong")
    


try:
    print(a/r)
except ZeroDivisionError as e:
    print(e)
    
except NameError as e:
    print(e)
    
except Exception as e:
    print(e)
    
except:
    print("asaa")
    
finally:
    print("closed")
    

print('.......................................................................')

# File handling
try:
    f = open('day1.txt', 'r')
    print(f.read())
    f.close()

except FileNotFoundError as e:
    print(e)
    
    
# try:
#     f = open('sarina.txt', 'w')
#     f.write("Written from file handling")
#     f.close()
# except Exception as e:
#     print(e)


try:
    f = open('sarina.txt', 'a')
    f.write("\n Append from \t file handling")
    f.close()
except Exception as e:
    print(e)



try:
    with open('git.py', 'r') as f:
        print(f.read())
except Exception as e:
    print(e)


import csv

try:
    with open('data.csv', 'r') as f:
        result = csv.reader(f)
        for i in result:
            print(i)
    
except Exception as e:
    print(e)


data = [['Hyeri','Nepal', 17, 123],['Asaa', 'India', 16, 234]]

try:
    with open('data.csv', 'a', newline="") as f:
        result = csv.writer(f)
        result.writerows(data)
    
except Exception as e:
    print(e)
    
import json
try:
    with open('data.json', 'r') as f:
        # result = json.load(f)
        result = f.read()
        print(result['name'])
        print(result.get('test'))
        
except Exception as e:
    print(e)
    
    

data = {"name": "Sarina", "age": 22}

with open("data.json", "w") as file:
    json.dump(data, file, indent=10)