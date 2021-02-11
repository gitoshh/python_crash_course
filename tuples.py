# An ordered collection that is unchangable. Allows duplicate members

# creating a tuple
fruits = ('Apples', 'oranges', 'Grapes')
# fruits = tuple(('Apples', 'oranges', 'Grapes')

# single value use a trailing comma
fruits2 = ('Apples',)

print(fruits2)
print(len(fruits2))
print(type(fruits2))


# Sets - An unordered and unindexed collection with no duplicate members

# creating a set
fruit_set = {'Apples', 'Mangoes', 'Oranges'}
print(fruit_set)

fruit_set.add('Pears')
print(fruit_set)

fruit_set.remove('Apples')
print(fruit_set)

fruit_set.clear()
print(fruit_set)

del fruit_set
print(fruit_set)
