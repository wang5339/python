list=["a","b","c"]
list2=["x","y","z"]
for i in list2:
    if(i!='x' and i!='z'):
        d=i
for i in list2:
    if(i!=d and i!='x'):
        e=i
for i in list2:
    if(i!=e and i!=d):
        f=i
print("a--{0},b--{1},c--{2}".format(d,e,f))