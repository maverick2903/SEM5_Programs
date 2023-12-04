
import json
from pprint import pprint

def load_data():
    with open('mobiledata.json', 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('mobiledata.json', 'w') as file:
        json.dump(data, file, indent=2)

def insert_user(data, user):
    data['users'].append(user)
    save_data(data)

def delete_user(data, user_id):
    deleted_user = next((user for user in data['users'] if user['id'] == user_id), None)
    data['users'] = [user for user in data['users'] if user['id'] != user_id]
    save_data(data)
    return deleted_user

def query_user(data, user_id):
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    return user

def alter_user(data, user_id, new_data):
    user_index = next((index for index, user in enumerate(data['users']) if user['id'] == user_id), None)
    if user_index is not None:
        data['users'][user_index].update(new_data)
        save_data(data)
        return data['users'][user_index]
    else:
        print(f"User with ID {user_id} not found.")

# Example usage:
data = load_data()

# Delete user with ID 3
deleted_user = delete_user(data, 3)
print("Deleted User:")
pprint(deleted_user)

# Query user with ID 4
queried_user = query_user(data, 4)
print("\nQueried User:")
pprint(queried_user['email'])

alter_data = {
    "age": 26,
    "email": "john.doe@example.com"
}
print("\nAltered data:", alter_user(data, 1, alter_data))

# Pretty print the entire data
print("\nUpdated User Data:")
pprint(data)
