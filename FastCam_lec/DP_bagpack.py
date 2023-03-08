# 12865 평범한 배낭
def bagpack(n, k, l):
    d = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(k+1):
            if j+l[i - 1][0] <= k:
                d[i][j+l[i - 1][0]] = max(d[i][j] + l[i - 1][1], d[i][j+l[i - 1][0]])
    return d

def bagpack2(n, k, l): # 이렇게 1차원 리스트로는 풀 수 없다. (반례:4 10 11 12 13 14)
    d = [0]*(k+1)
    for j in range(k+1):
        for i in range(n):
            if j+l[i][0] <= k:
                d[j+l[i][0]] = max(d[j] + l[i][1], d[j+l[i][0]])
    return max(d)

n, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
print(bagpack(n, k, l))