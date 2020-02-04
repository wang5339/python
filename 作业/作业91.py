s={"a":1,"b":2,"c":0}
x=s.copy()
f=sorted(x.items(),key=lambda g:g[1])
print(f)