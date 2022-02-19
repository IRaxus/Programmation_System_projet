# reading and writing  a+
with open(r'DemoG', "r+") as fp:
    fp.seek(0, 2)
    fp.write("\nADD THIS TO THE END OF THE FILE :)")
    fp.seek(0)
    print(fp.read())