# 9251 LCS
def lcs(n, m, nl, ml):
    d = 0
    maxd = 0
    i = 0
    while 0<= i < nl:
        for j in range(ml):
            if n[i] == m[j]:
                d += 1
            i += 1
        maxd = max(d, maxd)
        d = 0
    return maxd

def answersheet(n, m, nl, ml):
    d = [[0]*(nl+1) for _ in range(ml+1)]
    for i in range(1, nl):
        for j in range(1, ml):
            if n[i] == m[j]:
                d[j][i] = d[j-1][i-1] +1
            else:
                d[j][i] = max(d[j-1][i], d[j][i-1])
    return d[-1][-1]

n = input()
m = input()
nl, ml = len(n), len(m)
print(answersheet(n, m, nl, ml))
# if nl > ml:
#     print(lcs(n, m, nl, ml))
# else:
#     print(lcs(m,n, ml, nl))