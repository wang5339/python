a=list(map(int,input("请输入三个数字，用空格隔开：").split()))
b=max(a)
d=min(a)
for i in a:
    if(i!=b)and(i!=d):
        c=i
print("{0},{1},{2}".format(b,c,d))