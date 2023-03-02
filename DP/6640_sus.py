# Suspicious Stocks
def stock(d,m,l): # 이거가 안되는 이유 : 파는개수도 중요하기때문에 2에파는거보다 1에파는게 더 이득
    mind = [40001]*d
    maxd = [0]*d
    start = False
    for i in range(d):
        if start == True:
            maxd[i] = max(l[i], maxd[i-1])
            if mind[i-1] > l[i]:
                mind[i] = l[i]
                maxd[i] = 0
            else:
                mind[i] = mind[i-1]
        if l[i]<= m and start == False:
            start = True
            mind[i] = l[i]

    cha = [(maxv-minv) for minv, maxv in zip(mind, maxd)]
    f = lambda i: cha[i]
    idx = max(range(d), key = f)
    return ((m//mind[idx])*maxd[idx] + (m%mind[idx]))-m

def stock(d,m,l):
    gae = [0]*(d+1)
    don = [0]*(d+1)
    nam = 0
    for i in range(1, d+1):
        if gae[i-1] != 0:
            don[i] = max(l[i-1], don[i-1])
        if m >= l[i-1] and i != d:
            gae[i] = m // l[i - 1]
            if gae[i-1] < gae[i]:
                nam = m%l[i-1]
                don[i] = l[i-1]
            else:
                gae[i] = gae[i-1]
        else:
            gae[i] = gae[i-1]
            don[i] = don[i-1]
    profit = [(g*mon) for g, mon in zip(gae, don)]
    return max(profit)+nam -m

while True:
    d = input()
    if d == '0':
        break
    d, m = map(int, d.split())
    l = list(map(int, input().split()))
    out = stock(d,m,l)
    if out <= 0:
        print(0)
    else:
        print(out)