a = list(eval(input()))
maxi = max(a)
a.remove(maxi)
mini = min(a)
a.remove(mini)
a.insert(0, maxi)
a.insert(-1, mini)
print(a)