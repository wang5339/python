h=100
s=0
for i in range(0,10):
    s=h+s
    h=h/2
    if(i!=9):
        s=h+s
print("{0},{1}".format(s,h))