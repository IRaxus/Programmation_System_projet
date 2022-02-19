


f = open('DemoG', 'r', encoding = 'utf-8')
print(f.read(6),"\n")    # read the first 10 data
print(f.read(10))    # read the next 4 data
print(f.read())     # read in the rest till end of file
print(f.read())  # further reading returns empty sting
