# Suspicious Stocks
def stock(d,m,l): # 4 3 1 2
    dp = [[0] * (d+1) for _ in range(2)]
    dp[0][0] = m
    for i in range(d):
        if l[i] <= dp[0][i]:
            dp[1][i+1] = max(dp[1][i], dp[0][i] // l[i]) # 개수
            dp[0][i+1] = dp[0][i] - (l[i]*dp[1][i+1]) # 가격
        else:
            dp[0][i+1] = max(d[0][i], dp[0][i] + dp[1][i] * l[i+1])
    return m

while True:
    d = input()
    if d == '0':
        break
    d, m = map(int, d.split())
    l = list(map(int, input().split()))
    out = stock(d,m,l)
    out -= m
    if out <= 0:
        print(0)
    else:
        print(out)