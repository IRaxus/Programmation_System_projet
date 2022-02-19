
f = open('DemoG', 'r+')

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())

print_all(f)
rewind(f)
print_a_line(1,f)
