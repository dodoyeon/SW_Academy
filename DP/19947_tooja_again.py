# 투자의 귀재 배주형 다시...
def tooja(h, y):
    d = [0]*(y+1)
    d[0] = h
    for i in range(1, y+1):
        d[i] = int(1.05*d[i-1])
        if i >= 3:
            d[i] = max(d[i], int(1.2*d[i-3]))
        if i >= 5:
            d[i] = max(d[i], int(1.35*d[i-5]))
    return int(d[-1])

h, y = map(int, input().split())
print(tooja(h, y))