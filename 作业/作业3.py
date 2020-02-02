import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100)and(y*y==i+268):
        print("{0}".format(i))
'''n = 0
while (n+1)**2-n*n<=168 :
    n+=1

for i in range((n+1)**2):
    if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5) and i-100>0:
        print('可能存在的数是：',i-100)'''