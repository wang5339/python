def a(s, i, j):
    t = s[i]
    s[i] = s[j]
    s[j] = t
def p(s, start):     
    if s is None or start < 0:
        return
    if start == len(s) - 1:
        print("".join(s))
    else:
        i = start
        while i < len(s):
            a(s, start, i)               
            p(s, start + 1)      
            a(s, start, i)               
            i += 1
s = input()
s = list(s)