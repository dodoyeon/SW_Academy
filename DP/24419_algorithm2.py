def num_compare(n):
    d = [[0] * n for _ in range(n)]
    num = 2*n-1
    for i in range(n):
        d[0][i] = 1
    for i in range(1, n):
        d[i][0] = 1
    for i in range(1, n):
        for j in range(1, n):
            d[j][i] = d[j-1][i]+d[j][i-1]
            num += d[j][i]
    return (num+1)%(int(1e9)+7), (n**2)%(int(1e9)+7)

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
print(*num_compare(n), sep=' ')