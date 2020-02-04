list1 = list(map(int,input().split()))
m=int(input())
n=len(list1)
list2=[]
for i in range(m-n,m):
    list2.append(list1[i])
for i in range(m-n):
    list2.append(list1[i])
print(list2)

