# functionality for creating, reading and deleting files.

# open File
myFile = open('myfile.txt', 'w')
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Openung mode: ', myFile.mode)

myFile.write('I love python')
myFile.write('and Javascript')
myFile.close()

# Appending to files
myFile = open('myfile.txt', 'a')
myFile.write(' I also love Php')
myFile.close()


# Reading from files
myFile = open('myfile.txt', 'r+')
text = myFile.read()
print(text)
