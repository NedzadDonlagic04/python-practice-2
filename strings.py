def indexCharOutput(name):
    if name.isalpha()==True:
        print('The index for each letter is:')
        index=0
        for letter in name:
            print(index,'-',letter)
            index+=1
    else:
        print('The name you entered has invalid characters!')
        print('Try again!')


name=input('Enter your name:')
indexCharOutput(name)
print('Your name has',len(name),'characters')
