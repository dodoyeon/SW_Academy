# 효율적인 화폐구성 (나동빈 문제)
def goosung(n, m, l):
    d = [0]*(m+1)
    for i in range(1, m+1):
        for j in range(n):
            if i%l[j] == 0:
                d[i] = i//l[j]
            if i>=l[j] and d[i-l[j]] != 0:
                d[i] = min(d[i-l[j]]+1, d[i])
    if d[m] == 0:
        return -1
    return d[m]

def goosung_answersheet(n, m, l):
    d = [10001]*(m+1)
    d[0] = 0
    for j in range(n):
        for i in range(1, m+1):
            if i >= l[j] and d[i-l[j]] != 10001:
                d[i] = min(d[i], d[i-l[j]]+1)
    if d[m] == 10001:
        return -1
    return d[m]

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
new_l = [i for i in l if i <= m]
n = len(new_l)
print(goosung_answersheet(n, m, l))