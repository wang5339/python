n = [1, 2, 3, 4, 1, 3, 2, 4, 5, 7, 7, 6, 6]
for i in range(len(n)):
    if n.count(n[i]) == 1:
        print('n[%d]: %d' % (i, n[i]))
        break