# In python functions are defined with the def
# keyword and the body is defined with indentations
# the value inside the () is a parameter and the value
# we pass it is called an argument
# There are 2 types of functions
# Built in functions that are a part of python
# User defined functions we make ourselves, an example
# of which is seen below

from cgi import print_arguments


def outputHello():
    print('Hello')

outputHello()
# This outputHello function is also known as a void or
# not fruitful function since it does not return anything
# Same goes for the function below

def outputName(name):
    print('My name is',name)

outputName('Chad')

# The function below is known as a fruitful function
# because it returns a value

def return5():
    return 5

print(return5())

five=return5()
print(five)

# Just like other programming languages when the code
# runs into the return statement, the execution of that
# block of code comes to a stop and the value is returned
# to the function

# Correction about line 15, a void function returns None
# as shown below

print( type(outputHello()) )

# None is just the way python defines something as empty