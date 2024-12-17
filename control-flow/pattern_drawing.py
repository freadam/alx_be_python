size = int (input("Enter the size of the pattern: "))

for j in range(0,size):
    for i in range (0,size):
        if i < size-1:
            print("*", end="")
        else:
            print("*", end="\n")
