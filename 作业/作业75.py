def han(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if (x[i]!=x[j]):
                continue
            else:
                return i
n=input()
print(han(n)) 