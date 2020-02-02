n=int(input())
s=0
for i in range(2,n):
    a=0
    for j in range(2,i):
        if(i%j==0):
            a=1
    if (a==0):
        s+=1
print(s)