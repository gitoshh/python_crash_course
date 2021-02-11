# A module is a file containing a set of functions to include in your app. There are core modules, modules you
# can install using pip package manager as well as custom modules

# importing a core python module
# import datetime
# import time

from validator import validate_email
from camelcase import CamelCase
from datetime import date
from time import time

# today = datetime.date.today()
today = date.today()
print(today)

# timestamp = time.time()
timestamp = time()
print(timestamp)

# Pip module

c = CamelCase()
print(c.hump('hello godwin gitonga'))


# Custom module

email = 'godwin@mail.co'

if validate_email(email):
    print('Email is good')
else:
    print('Email is bad')
