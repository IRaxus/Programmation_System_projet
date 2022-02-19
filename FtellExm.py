#Open a file
f = open('DemoG', 'r+')
data = f.read(7)
print('Read String is : ', data)

#Check current position
position = f.tell()
print('Current file position : ', position)