# commonly used with APIs

import json

# Converting json to dicts
# sample json
user_json = '{"first_name": "John", "last_name": "Doe", "age": 30}'
user = json.loads(user_json)

print(user)
print(user['first_name'])

car = {"make": "Ford", "model": "Mustang"}
car_json = json.dumps(car)

print(car_json)
