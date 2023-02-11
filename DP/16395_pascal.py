def pascal(n, k):
    if n <= 2:
        return 1
    d = [0] *((n*(n+1)//2)+1)
    d[1] = 1
    d[2], d[3] = 1, 1
    for i in range(3, n+1):
        for j in range(1, i+1):
            idx = (i*(i-1)//2) + j
            if j == 1 or j == i:
                d[idx] = 1
            else:
                jdx = (i-2)*(i-1)//2
                d[idx] = d[jdx+(j-1)]+d[jdx+j]
    return d[(n*(n-1)//2)+k]

n, k = map(int, input().split())
print(pascal(n, k))