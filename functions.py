# Function is a block of called that only runs when called.

# creating a function
def sayHi(name='John Doe'):
    print(f'Hi {name}')


sayHi()


# Return values
def getSum(num1, num2):
    return num1 + num2


num = getSum(3, 4)
print(num)

# Lambda function - Small anonymous function that takes in multiple args and can only have one expression
getSum = lambda num1, num2 : num1 + num2
print(getSum(40, 50))
