def f(n):
    return len(list(set(n))) != len(n)
n = list(eval(input()))
print(f(n))