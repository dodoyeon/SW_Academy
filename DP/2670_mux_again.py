def mux_answersheet(n, l):
    d = l[:]
    for i in range(1, n):
        if d[i-1] >= 1:
            d[i] *= d[i-1]
    return max(d)

def mux(n, l):
    d = [0]*n
    d[0] = l[0]
    for i in range(1, n):
        if d[i-1] >= 1:
            d[i] = d[i-1]*l[i]
        else:
            d[i] = l[i]
    return max(d)

n = int(input())
l = [float(input()) for _ in range(n)]
print('{:.3f}'.format(mux(n, l)))