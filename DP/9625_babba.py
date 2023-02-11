def babba(k):
    d = [1, 0]
    for i in range(k):
        temp = [0, 0]
        temp[1] = (d[0]+d[1])
        temp[0] = d[1]
        d = temp
    return d
k = int(input())
print(*babba(k))