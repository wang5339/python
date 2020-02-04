x=input()
f=open("second.txt","w")
for i in x:
    if i!="#":
        f.write(i)
f.close()