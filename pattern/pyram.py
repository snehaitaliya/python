a=2
for i in range(1,6):
    for j in range(5-i,0,-1):
        print(" ",end="")
    for j in range(i,i*2):
        print(j,end="")
   # for j in range(2,i-1):
    #    print(j,end="")
    #for j in range(i,0,-1):
     #   print(j,end="")

    print()
    
for i in range(6,i,-1):
    for j in range(i,i*2-1):
        print(j,end="")

    print()
