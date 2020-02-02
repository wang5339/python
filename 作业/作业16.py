x=int(input())
a=x
print(x,end="")
print("=",end="")
while(a!=1):
    for i in range(2,a+1):
        if(a/i==a//i):
            print(i,end="")
            if(i!=a):
                print("*",end="")
            a=a//i
            break

        