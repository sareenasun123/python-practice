import requests 

data_url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url=data_url)
if r.status_code == 200:
    data = r.json()
    for i in data:
        print(i['userId'], i['title'])
    print(type(data))
print(r)