def c(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
    return a
for i in range(20):
    print(c(i),end=" ")
