import functionPractice as funcPr

def main():
    list1=[3,-5,1,6,7]
    print('Biggest number in the list:',funcPr.biggestVal(list1))
    print('Smallest number in the list:',funcPr.smallestVal(list1))
    print('List before sort:',list1)
    funcPr.sortedList(list1)
    print('List after sort:',list1)

if __name__=='__main__':
    main()