def sugardelivery(n):
    if n == 3 or n == 5:
        return 1
    elif n == 4:
        return -1
    d = [n] * (n + 1)
    d[3], d[5] = 1, 1
    for i in range(3, n+1):
        if d[i-3] != 0:
            d[i] = min(d[i], d[i-3]+1)
        if d[i-5] != 0:
            d[i] = min(d[i], d[i-5]+1)
    if d[n] == n:
        return -1
    else:
        return d[n]

n = int(input())
print(sugardelivery(n))