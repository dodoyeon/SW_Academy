# 투자의 귀재 배주현 다시...
def tooja(h, y):
    d = [0]*(y+1)
    d[0] = h
    for i in range(1, y+1):
        d[i] = int(d[i-1]*1.05)
        if i >= 3:
            d[i] = max(int(d[i-3]*1.2), d[i])
        if i >= 5:
            d[i] = max(int(d[i-5]*1.35), int(d[i-3]*1.2), d[i])
    return d[y]

h, y = map(int, input().split())
print(tooja(h, y))