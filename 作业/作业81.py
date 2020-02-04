x=list(input())
for i in range(len(x)):
    x[i]=(int(x[i])+5)%10
print(x)