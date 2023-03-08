# 01 타일
def tile(n): # 이렇게 하면 메모리 초과
    if n <= 1:
        return n
    d = [0]*n
    d[0], d[1] = 1, 2
    for i in range(2, n):
        d[i] = d[i-1]+d[i-2]
    return d[-1]

def tile1(n):
    if n <= 2:
        return n
    d0, d1 = 1, 2
    for _ in range(2, n):
        d1, d0 = (d0+d1)%15746, d1%15746
    return d1

n = int(input())
print(tile1(n))