name, age = ('Godi', 28)

# output
print('Hello my name is ' + name + 'and I am ' + str(age))

# string formating
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-string
print(f'My name is {name} and I am {age}')

# String methods
s = 'Hello world'

# capitalize
print(s.capitalize())
print(s.upper())
print(s.replace('world', 'everyone'))
print(s.split())
print(s.find('r'))
print(s.endswith('d'))
