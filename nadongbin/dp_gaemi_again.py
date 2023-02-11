def gaemi(n, l):
    d = [0]*n
    d[0] = l[0]
    d[1] = max(l[0], l[1])
    for i in range(2, n): # [3, 4, 5, 6, 1, 2,] 3 4 8 10 10 12
        d[i] = max(d[i-2]+l[i], d[i-1])
    return d[n-1]
n = int(input())
l = list(map(int, input().split()))
print(gaemi(n, l))