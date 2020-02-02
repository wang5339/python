d=int(input("请输入几个数相加:"))
a=int(input("\n请输入相加的数字:"))
b=a
s=0
for i in range(0,d):
    s=s+a
    a=a*10+b
print(s)