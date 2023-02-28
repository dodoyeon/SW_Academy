def numseq(n, l):
    d = [[0]*n for _ in range(2)]
    d[0][0], d[1][0] = 1, 1
    for i in range(1, n):
        if l[i-1] <= l[i]:
            d[0][i] = d[0][i-1]+1
        else:
            d[0][i] = 1
        if l[i-1] >= l[i]:
            d[1][i] = d[1][i-1]+1
        else:
            d[1][i] = 1
    return max(max(d[0]), max(d[1]))

n = int(input())
l = list(map(int, input().split()))
print(numseq(n, l))