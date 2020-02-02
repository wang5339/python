a=1
b=2
s=0
for i in range(0,20):
    s=s+b/a
    a,b=b,a+b
print(s)