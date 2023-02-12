# 수열
def longseq(l, n):
    d = [0]*n
    d[0], d[1] = 1, 2
    for i in range(1, n):
        if l[i] >= l[i-1] >= l[i-2]:
            d[i] = d[i-1]+1
        if l[i] <= l[i-1] <= l[i-2]:
            d
        else:
            d[i] = d[i - 1] + 1
    return max(d)

n = int(input())
l = list(map(int, input().split()))
print(longseq(l, n))