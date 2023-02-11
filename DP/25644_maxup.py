# 최대 상승
def maxup(n, l):
    d = [0]*(n+1)
    mint = 0
    for i in range(1, n):
        if l[mint] > l[i]:
            mint = i
        elif l[mint] < l[i]:
            d[i] = (l[i]-l[mint])
    return max(d)

n = int(input())
l = list(map(int, input().split()))
print(maxup(n, l))