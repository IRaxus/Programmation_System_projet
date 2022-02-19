L = ["HElLO SIR \n", "MORE DIFFERENT INPUT \n", "WE LIVE IN MOROCCO \n"]

# Writing to file
with open("DemoG", "w") as f:
    # Writing data to a file
    f.write("Hello \n")
    f.writelines(L)
