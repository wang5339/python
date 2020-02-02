x=input()
z=0
k=0
s=0
f=0
for i in x:
    if("0"<=i<="9"):
        s=s+1 
    elif("a"<=i<="z" or "A"<=i<="Z"):
        z=z+1
    elif(i==" "):
        k=k+1
    else:
        f=f+1
print("数字:{0}字母:{1}空格:{2}字符:{3}".format(s,z,k,f))