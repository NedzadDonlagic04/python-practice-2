fileName=input('Enter the name of the file:')

try:
    fileHandler=open(fileName)
except:
    print('File doesn\'t exist!')
    quit()

print('All the comments in the file are:')

for comment in fileHandler:
    if comment.startswith('#') is True:
        comment=comment.rstrip()
        print(comment)

fileHandler2=open('README.md')
text=fileHandler2.read()
print(text)

# In this last part we are reading the entire
# file and storing it inside the text variable
# which is ok for small file sizes but for larger
# sized ones it is recommended to read line by line