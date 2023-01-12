# 부녀회장이 될테야
def dp(k, n):
    for j in range(1, k+1):
        for i in range(n):
            if dpmem[j][i] == 0:
                dpmem[j][i] = sum(dpmem[j-1][:(i+1)])
    return dpmem[k][(n-1)]

t = int(input())
dpmem = [[0]*14 for _ in range(15)]
dpmem.insert(0, [(i+1) for i in range(14)])
for i in range(t):
    k = int(input())
    n = int(input())
    print(dp(k, n))