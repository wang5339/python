for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print("\n")
for i in range(1,4):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(5-(i-1)*2,0,-1):
        print("*",end="")
    print("\n")