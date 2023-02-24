# Suspicious Stocks
def stock(d,m,l):
    dp = [[0]*(d+1) for _ in range(2)]
    dp[0][0] = m
    for i in range(d):
        price = dp[0]
        gae = dp[1]
        if l[i] <= price[i]:
            nowgae = m // l[i]
            if gae[i] > nowgae:
                gae[i+1] = gae[i]
                price[i+1] = price[i]
            else:
                gae[i+1] = nowgae
                price[i+1] = m-(nowgae*l[i])
        else:
            m = max(m, gae[i]*l[i]+price[i])
            price[i+1], gae[i+1] = price[i], gae[i]
    return m

def stock2(d, m, l):
    dp = [[0]*(d+1) for _ in range(2)]
    dp[0][0] = m
    for i in range(d):
        minm = dp[0]
        maxm = dp[1]
        if l[i] < minm[i]:
            minm[i+1] = l[i]
        else:
            minm[i+1] = minm[i]
        if l[i] > maxm[i]:
            maxm[i+1] = l[i]
        else:
            maxm[i+1] = maxm[i]
    profit = (m//minm)*maxm
    return profit

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