import requests 
import json
list_req = []
for x in range(1,6):
  r = requests.get(url = "https://jsonplaceholder.typicode.com/todos/" + str(x))
  list_req.append(r)
for i in list_req:
    print(i.json())
