size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Please enter a positive integer")
else:
    row = 0
    while row < size:
        col = 0
        while col < size:
            print("*", end = " ")
            col +=1
        print()
        row +=1