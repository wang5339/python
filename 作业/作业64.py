n=int(input())
list1=[i+1 for i in range(n)]
count=0
x=n
i=0
while(n>1):
    if (list1[i]!=0):
        count=count+1
    if(count==3):
        count=0
        list1[i]=0
        n=n-1
    i=i+1
    if(i==x):
        i=0
for i in range(x):
    if(list1[i]!=0):
        print(list1[i])
      