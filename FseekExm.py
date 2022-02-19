#Open a file
f = open('DemoG', 'r+')
data = f.read(7);
print('Read String is : ', data)

#Reposition pointer at the beginning once again
position = f.seek(0, 0);
data = f.read(16);
print('Again read String is : ', data)