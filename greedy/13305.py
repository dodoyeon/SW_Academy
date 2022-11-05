# 주유소
n = int(input())
dist = list(map(int, input().split()))
liter = list(map(int, input().split()))
num = 0
il, id, d = 0, 0, 0
while True:
    if il == (n-1):
        break
    d += dist[id]
    if liter[il]<liter[id+1]:
        id += 1
        if id == (n-1):
            num += d * liter[il]
            break
    elif liter[il]>=liter[id+1]:
        num += d*liter[il]
        id += 1
        il = id
        d = 0
print(num)