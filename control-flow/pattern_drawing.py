size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Please enter a positive integer")
else:
    for row in range(size):
        for col in range(size):
            print("*", end = " ")
        print()
