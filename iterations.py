# Finding the smallest number in the list

smallest=None
for item in [5,10,3,9,-4]:
    if smallest==None or smallest>item:
        smallest=item 

print('The smallest number is',smallest)

# Finding the biggest number in the list

biggest=None
for item in [5,10,3,9,-4]:
    if biggest==None or biggest<item:
        biggest=item 

print('The biggest number is',biggest)

# is and is not are like === and !== in Javascript
# from what I understand == and != compare the values
# with type conversion while is and is not have no type
# conversion
# Example below

print('5==5.0 is',5==5.0)
print('5!=5.0 is',5!=5.0)

print('5 is 5.0 is',5 is 5.0)
print('5 is not 5.0 is',5 is not 5.0)