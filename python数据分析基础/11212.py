for i in range(10):
    x=int (input())
    list.append(x)
for i in range(9):
    for j in range(10-1-i):
        if(list[i]>list[j+1]):
            k=list[i]
            list[j]=list[j+1]
            list[j+1]=k
print(list)