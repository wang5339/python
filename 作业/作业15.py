for i in range(100,1000):
    a=i%100%10
    b=i//10%10
    c=i//100
    if(i==a**3+b**3+c**3):
        print(i)