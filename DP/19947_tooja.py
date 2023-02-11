# 투자의 귀재 배주형
def tooja(h, y):
    d = [0]*(y+1)
    d[0] = h
    for i in range(1, y+1):
        d[i] = int(1.05*d[i-1])
        if i >= 3:# i%3 == 0:
            d[i] = max(d[i], int(1.2*d[i-3])) # ((i//3)-1)*3
        if i >= 5: # i%5 == 0:
            d[i] = max(d[i], int(1.2*d[i-3]), int(1.35 * d[i-5])) # ((i//5) - 1) * 5
    return d[y]

h, y = map(int, input().split())
print(int(tooja(h, y)))