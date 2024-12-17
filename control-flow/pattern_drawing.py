size = int (input("Enter the size of the pattern: "))
outer = 0 
while outer < size:
    for i in range (size):
        if i < size-1 :
            print("*", end="")
        else:
            print("*", end="\n")
    outer += 1
