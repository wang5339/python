def han(a):
    if(a<0):
        print("error")
    elif(a==0 or a==1):
        s=1
    else:
        s=a*han(a-1)
    return(s)
print(han(5)) 