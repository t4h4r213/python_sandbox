# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
from datetime import date
from time import time

# Pip module
# from camelcase import CamelCase

# Custom module
from validator import validate_email

today = date.today()
timestamp = time()

# c = CamelCase()
# result = c.hump("hello there world")


email = "taharbelhouchat213#gmail.com"
if validate_email(email):
    print("Email is valid")
else:
    print("Email is bad")
