a=['a','b','c','d','e','d']
b=[1,2,3,4,5,6]
c={}  
for i in range(len(a)):
    if a[i] not in c:
        c[a[i]]=b[i]
print(c)