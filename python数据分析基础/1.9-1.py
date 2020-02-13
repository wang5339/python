a=["as",'cd','asd']
b=['1','2','3']
c=['45','5455','67']
d=a+b+c
for i in range(len(d)):
    print("{0:d}:{1:s}".format(i,d[i]))