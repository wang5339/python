a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==2 and j==2:
            print(str(a[i][j])+'\n')
        else:
            print(str(a[i][j])+',',end="")