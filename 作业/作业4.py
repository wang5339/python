n=int(input("请输入年："))
y=int(input("请输入月："))
r=int(input("请输入日："))
if (((n%4==0 )and (n%100!=0))or(n%400==0) ):
	a = 1
else :
	a = 0
b=[0,0,31,59,90,120,151,181,212,243,273,304,334]
if(a==1):
    if(y>2):
        s=b[y]+1+r
    else:
        s=b[y]+r
else:
    s=b[y]+r
print("这是第{0}天！".format(s))