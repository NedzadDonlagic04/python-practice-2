# Some basic python operators
# + addition

addition = 2 + 3
print(addition)

# - subtraction
subtraction = 5 - 2
print(subtraction)

# * multiplication
multiplication = 6 * 3
print(multiplication)

# / floating division
division = 12 / 3
print(division)

# ** power
power = 6 ** 2
print(power)

# These are the basic ones I'll use for now

# The type function says what type a value is
print(type(5))
print(type(5.0))
print(type('Hello'))
print(type("There"))
print(type(True))
print(type(False))

# There is also implicit and explicit type conversion
# In the print below the 3 (type int) is converted
# implicitly into a float before the addition can be 
# performed
print( 5.0 + 3)

# In the print below it is done explicitly
print( 5.0 + float(3))

# Usually,from my experience, you leave the implicit 
# things be for the sake of cleaner code, unless it's
# really needed to explicitly convert it, like in the
# print below, we can't add an integer to a string 
# unless we explicitly make the string into an int
# (This will fail if the string has a non numeric 
# character)

# print( '123' + 5) 
# ^Bad

print( int('123') + 5)
# ^Good

# print( int('12A3') + 5)
# ^Bad

# if elif and else works just as if else if and else

age=input('Enter your age:')
age=int(age)
# ^Explicit conversion due to input returning a string

if age>=65 :
    print('Your bus ticket is free!')
elif age>=18 :
    print('You have to pay the full price of the ticket!')
else :
    print('You have to pay half the price of the ticket!')