x=int(input())
print(int((bin(x)[2:]).rjust(32,'0')[::-1],2))