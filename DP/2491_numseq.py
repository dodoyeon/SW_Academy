# 수열
def longseq(l, n):
    if n == 1:
        return 1
    d = [[0]*n for _ in range(2)]
    d[0][0], d[1][0] = 1, 1
    for i in range(1, n):
        if l[i-1] < l[i]:
            d[0][i] = d[0][i-1]+1
            d[1][i] = 1
        elif l[i-1] > l[i]:
            d[1][i] = d[1][i-1]+1
            d[0][i] = 1
        else:
            d[0][i] = d[0][i - 1] + 1
            d[1][i] = d[1][i - 1] + 1
    d0 = max(*d[0])
    d1 = max(*d[1])
    return max(d0, d1)

n = int(input())
l = list(map(int, input().split()))
print(longseq(l, n))