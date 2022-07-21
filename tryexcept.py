# The try and except block do as the following
# The code in the indentations of the try block is
# executed, but if an error occurs the block throws
# an exception, which means the code in the try block
# stops executing and gets skipped and the except block
# code gets executed

age=input('Enter your age:')
try:
    age=int(age)
    if age<0:
        print('Age can\'t be a negative number!')
    else:
        print('You are',age,'years old')
except:
    print('That wasn\'t a number!')

# Another way this can be done is with the isnumeric() 
# method
# As shown in the example below using the same code from
# above just without the try and except

age=input('Enter your age:')
if age.isnumeric() is True:
    age=int(age)
    if age<0:
        print('Age can\'t be a negative number!')
    else:
        print('You are',age,'years old')
else:
    print('That wasn\'t a number!')