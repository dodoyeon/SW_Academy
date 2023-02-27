# 1, 2, 3 더하기 ->중복순열
def onet2(n):
    if n < 3:
        return n
    d = [0]*n
    d[0], d[1], d[2] = 1, 2, 4
    for i in range(3, n):
        d[i] += d[i-1]
        d[i] += d[i-2]
        d[i] += d[i-3]
    return d[n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(onet2(n))