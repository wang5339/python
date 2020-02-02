list=[]
x=int(input())
for i in range(1,x+1):
    if(i%3==0 and i%5==0):
        list.append("FizzBuzz")
    elif(i%3==0):
        list.append("Fizz")
    elif(i%5==0):
        list.append("Buzz")
    else:
        list.append(i)
print(list)