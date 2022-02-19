def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

file = open('DemoG', 'rb')
print("File Size is:", getSize(file))