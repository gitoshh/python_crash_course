# create list
numbers = [1, 2, 3, 4]

numbers_using_constructor = list((1, 2, 3, 4))

fruits = ['mangoes', 'kiwis', 'avocado']

print(numbers, numbers_using_constructor)

print(fruits)
print(len(fruits))
fruits.append('strawberries')
print(fruits)
fruits.insert(2, 'pawpaw')
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)


fruits.pop(2)
print(fruits)
