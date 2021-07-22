import requests

  
list_req = []
for x in range(6):
  r = requests.get(url = "https://jsonplaceholder.typicode.com/todos/" + str(x))
  list_req.append(r)
  

for r in list_req:
    print(list(r.json()))