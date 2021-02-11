x, y = (10, 9)

if not x == y:
    print(f'{x} is not equal to {y}')

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{y} is equal than {x}')
else:
    print(f'{y} is greater than {x}')

# Membership operators
numbers = [1, 2, 3, 4]

# in
if 3 in numbers:
    print(3 in numbers)

# not in
if 8 not in numbers:
    print(8 not in numbers)

# Identity operators
a = 20
b = 20
if a is b:
    print(True)

if 8 is not b:
    print(False)
