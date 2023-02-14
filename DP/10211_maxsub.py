# Maximum Subarray
def maxsub(n, l):
    if n == 1:
        return l[0]
    d = [[0]*n for _ in range(2)]
    for i in range(n):
        d[0][i] = sum(l[:(i+1)])
        d[1][i] = sum(l[i:])
    for i in range(n):
        val0, val1 = d[0][i], d[1][n-1-i]
        for j in range(i):
            val0 -= l[j]
            val1 -= l[n-1-j]
            d[0][i] = max(d[0][i], val0)
            d[1][n-1-i] = max(d[1][n-1-i], val1)
    d0 = max(*d[0])
    d1 = max(*d[1])
    return max(d0, d1)

def maxsub_answersheet(n, l):
    d = l
    for i in range(1, n):
        if d[i-1] > 0:
            d[i] += d[i-1]
    return max(d)

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(maxsub_answersheet(n, l))