for i in range(101,201):
    a=0
    for j in range(2,i):
        if(i%j==0):
            a=1
    if(a==0):
        print(i)
