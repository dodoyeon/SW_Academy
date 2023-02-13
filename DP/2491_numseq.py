# 수열
def longseq(l, n):
    d = [0]*n
    s = [0]*n
    if n < 3:
        return n
    d[0], d[1] = 1, 2
    if l[0] > l[1]:
        s[0], s[1] = -1
    elif l[0] < l[1]:
        s[0], s[1] = 1

    for i in range(2, n):
        if l[i-1] == l[i]:
            if s[i-1] != 0:
                d[i] = d[i - 1] + 1
        elif l[i-1] < l[i] and s[i-1] > 0:
            d[i] = d[i - 1] + 1
            s[i] = 1
        elif l[i - 1] > l[i] and s[i-1] < 0:
            d[i] = d[i - 1] + 1
            s[i] = -1
        else:
            d[i] = 1
    return max(d)

n = int(input())
l = list(map(int, input().split()))
print(longseq(l, n))