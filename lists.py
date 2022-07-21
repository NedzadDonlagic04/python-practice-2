# Lists represent a container of other objects/values
# They are similar to arrays but the python documentation
# calls them lists so I will as well when using python
# Lists start and end with [] and are accessed via indexing

list1=[1,2,3,4,5]
print('list1 =',list1)
print('list1 has',len(list1),'elements')

# The len (short for length) function gives us the number of
# items a container has

print(range(3))
print(range(len(list1)))

# The range function gives us the range from 0 up until the 
# passed value but not including it, this can be very useful
# if we wish to pass through a list (or some other index based
# container) because we will know the index of each item,an 
# example of this can be seen below

print('\nEvery even list1 item is:')
list1Len=len(list1)

for index1 in range(list1Len):
    if index1%2!=0:
        print(list1[index1])

print('\nEvery odd list1 item is:')

for index2 in range(list1Len):
    if index2%2==0:
        print(list1[index2])

# There's also a lot of other useful functions that we can use
# with lists, such as

print('The biggest value of the list is',max(list1))
print('The smallest value of the list is',min(list1))
print('The sum of all the values in the list is',sum(list1))

# If there is a need to create an empty list, we can do it by 
# calling the list constructor like so

print('\nlist2')
list2=list()

list2.append(5)
list2.append(3)
list2.append(-5)

print(list2)

# append adds a new item to the end of the list

list2.sort()
print(list2)

# sort sorts the list in ascending order
# but if we want a descending order all we have to do is

list2.sort(reverse=True)
print(list2)

# A thing to note is that sort takes the original list
# and sorts it, if we want to just get the sorted list 
# returned we use the sorted

print('\nlist3')
list3=sorted(list2)
print(list3)

list3=sorted(list2,reverse=True)
print(list3)