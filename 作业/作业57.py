'''N = [1]
for i in range(10):  #打印10行
    print(N)
    N.append(0)
    N = [N[k] + N[k-1] for k in range(i+2)]'''
n=[1]
for i in range(10):
    l=n.copy()
    for j in range(len(l)):
        temp=str(l[j])
        l[j]=temp
    l=' '.join(l).center(50)
    print(l)
    n.append(0)
    n=[n[k]+n[k-1] for k in range(i+2)]