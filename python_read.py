#read method reads entire content of the file
with open('test.txt', 'r') as file:
    print(file.read())

 
#readline returns a single line as a string
with open('newfile.txt', 'r') as file:
    print(file.readline())
    