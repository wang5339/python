def han(a):
    if a==-1:
        return ''
    else:
        return x[a]+han(a-1)
x=input()
print(han(len(x)-1))