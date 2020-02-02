#两个变量值互换。
a,b=map(int ,input("请输入两个数字，以空格隔开").split())
a,b=b,a
print(a,b)