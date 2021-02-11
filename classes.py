# A class is a blueprint for creating objects

# creating classes
class User:

    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'Hello my name is {self.name} and I am {self.age}'

    def has_birtday(self):
        self.age += 1


class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'Hello my name is {self.name} and I am {self.age} and my balance is {self.balance}'


# initialize user object
brad = User('Brad', 'Brad@mail.co', 30)
brad.has_birtday()
print(brad.greeting())

janet = Customer('Brad', 'Brad@mail.co', 30)
janet.has_birtday()
janet.set_balance(500)
print(janet.greeting())
