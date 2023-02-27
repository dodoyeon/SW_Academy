# 다이나믹이 뭐에요?
def dp(n, m):
    if n ==1 or m == 1:
        return 1
    d = [[1]*n]
    for _ in range(m-1):
        newrow = [0]*n
        newrow[0] = 1
        d.append(newrow)
    d[1][1] = 3
    for i in range(1, n):
        for j in range(1, m):
            if i == 1 and j == 1:
                pass
            else:
                d[j][i] = (d[j-1][i]+d[j][i-1]+d[j-1][i-1])%int(1e9+7)
    return d[m-1][n-1]

n, m = map(int, input().split())
print(dp(n, m))