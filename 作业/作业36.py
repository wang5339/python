#请输入星期几的第一个字母来判断一下是星期几，
#如果第一个字母一样，则继续判断第二个字母。
x=input()
if (x=='m'):
    print("monday")
elif(x=="w"):
    print("wednesday")
elif(x=="f"):
    print("friday")
elif(x=="t"):
    x=input("请输入第二个字母：")
    if(x=="u"):
        print("tuesday")
    else:
        print("thursday")
elif(x=="s"):
    x=input("请输入第二个字母:")
    if (x=="a"):
        print("saturday")
    else:
        print("sunday")
        
        