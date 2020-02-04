list1=list(map(int,input("请输入7个数（1——50）").split()))
for i in list1:
    for j in range (i):
        print("*",end="")
    print("\n")
