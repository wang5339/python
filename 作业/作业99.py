d={}
f=open("爱丽莎.txt").read()
f=f.lower()
for ch in  '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}':
    f.replace(ch," ")
s=f.split()
for x in s:
    d[x]=d.get(x,0)+1
d_list=list(d.items())
d_list.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    print(d_list[i])
