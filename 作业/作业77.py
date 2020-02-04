# 求0—7所能组成的奇数个数。
for i in range(1,9):
    if (i==1):
        count=4
    elif (i==2):
        count=count*7
    else:
        count=count*8
print(count)