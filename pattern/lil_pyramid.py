 for i in range(1,4):
    for j in range(4-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")

    print()

for i in range(2,0,-1):
    for j in range(4-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")

    print()
