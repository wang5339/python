n = 1
while n:
    m = (5 * n + 1) / 4
    z = (5 * m + 1) / 4
    y = (5 * z + 1) / 4
    x = (5 * y + 1) / 4
    if int(x) == x and int(y) == y and int(z) == z and int(m) == m:
        break
    else:
        n += 1
print(int(5 * x + 1))