n = [2, 7, 11, 15]
t = int(input())
for i in range(4):
    for j in range(i + 1, 4):
        if n[i] == t - n[j]:
            print(i, j)