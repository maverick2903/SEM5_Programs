import json
from pprint import pprint

with open('test.json','r') as file:
    data = json.load(file)

pprint(data)
print()

print("Query")
query_id = 4
for i in range(len(data)):
    if i == query_id:
        print(data[i])

print()

print("Insert")
user = {'country': 'India', 'location': 'Delhi', 'name': 'Varun'}
data.append(user)
pprint(data)

print()

print("Delete")
delete_id = 3
for i in range(len(data)):
    if i == delete_id:
        data.remove(data[i])
        break

pprint(data)

print()

print("Update")
update_id = 1
update_json = {'country': 'USA', 'location': 'New York', 'name': 'Varun'}
for i in range(len(data)):
    if i == update_id:
        data[i].update(update_json)

pprint(data)