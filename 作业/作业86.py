f=open("first.txt")
f1=open("second.txt")
f2=open("third.txt","a+")
while True:
    line=f.readline()
    if len(line)==0:
        break
    f2.write(line)
f.close()
while True:
    line=f1.readline()
    if len(line)==0:
        break
    f2.write(line)
f1.close()
f2.close()