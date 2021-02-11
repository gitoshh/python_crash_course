# A collection that is unordered, changeable and indexed. No duplicate members

# Creating a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person, type(person))

person2 = dict(first_name='Jane',
               last_name='Doe')
print(person2, type(person2))

# Getting values
print(person2['first_name'])
print(person2.get('last_name'))

# Adding values
person2['phone'] = '5555-555'
print(person2)

# getting dictoniary keys
print(person2.keys())
print(person2.items())

# Copying dictionary
person3 = person2.copy()
print(person3)

# Removing attribs
del person3['phone']
print(person3)
person3.pop('last_name')
print(person3)
print(len(person3))

# clearing as dictionary
person3.clear()
print(len(person3))

# List of dictionaries
people = [{
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
},
    {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 30
}
]
print(people)
