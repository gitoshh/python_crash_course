# A loop is used to iterate over a sequence that is either a list, tuple, dictionary, set or string

# For loops
people = ['John', 'Paul', 'Sarah', 'Susan']

for person in people:
    print(f'current person: {person}')

print('\n')

for person in people:
    if person == 'Sarah':
        break
    print(f'current person: {person}')

print('\n')

for person in people:
    if person == 'Sarah':
        continue
    print(f'current person: {person}')

print('\n')

# Range
for i in range(len(people)):
    print(people[i])

print('\n')

for i in range(1, 12):
    print(i)

# While loops
count = 0

while count <= 10:
    print(f'count: {count}')
    count += 1
