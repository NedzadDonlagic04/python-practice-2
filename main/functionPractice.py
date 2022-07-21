# Defining the function biggestVal which for the passed
# list returns the biggest value inside of it
def biggestVal(list1):
    if len(list1) == 0:
        return 'The list is empty!'

    returnVal=list1[0]
    for item in list1:
        if returnVal<item:
            returnVal=item
    
    return returnVal

# Defining the function smallestVal which for the passed
# list returns the smallest value inside of it
def smallestVal(list1):
    if len(list1) == 0:
        return 'The list is empty!'

    returnVal=list1[0]
    for item in list1:
        if returnVal>item:
            returnVal=item
    
    return returnVal

# Defining the function sortedList which for the passed
# list sorts it in ascending order, if the reverse
# argument's value is set to True it will sort it in
# descending order, if it's set to any other value it 
# will output an error message
def sortedList(list1,reverse=None):
    listLen=len(list1)

    if listLen == 0:
        return 'The list is empty!'

    if reverse is None:
        for x in range(listLen):
            for y in range(x,listLen):
                if list1[x]>list1[y]:
                    list1[y]+=list1[x]
                    list1[x]=list1[y]-list1[x]
                    list1[y]=list1[y]-list1[x]
    elif reverse is True:
        for x in range(listLen):
            for y in range(x,listLen):
                if list1[x]<list1[y]:
                    list1[y]+=list1[x]
                    list1[x]=list1[y]-list1[x]
                    list1[y]=list1[y]-list1[x]
    else:
        print('Wrong argument passed to reverse!')

    