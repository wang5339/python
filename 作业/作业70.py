def han(n):
    s=0.0
    if(n%2==0):
        for i in range(1,n+1):
            if(i%2==0):
                s+=1/i
    else:
        for i in range(1,n+1):
            if(i%2!=0):
                s+=1/i
    return s
x=int(input())
print(han(x))