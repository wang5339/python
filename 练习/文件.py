"""s=assda
asdasd
asdasd
f=open("first.txt","w")
f.write(s)
f.close()
"""
f=open("first.txt")
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)
f.close()