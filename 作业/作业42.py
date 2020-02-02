# 求一个3*3矩阵主对角线元素之和。
l = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
s=0
for i in range(3): 
    for j in range(3):
        if i == j: 
            s+=l[i][j]
print ('对角线之和为%d'%s)
