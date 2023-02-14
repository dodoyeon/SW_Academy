# 자전거 묘기
def bike(l, n):
    d = [0]*n
    d[(n-1)] = 1
    for i in range(n-2, -1, -1):
        if l[i] == 0:
            d[i] = d[i+1] + 1
        else:
            idx = i+l[i]+1
            if idx <= (n-1):
                d[i] = d[idx]+1
            else:
                d[i] = d[(n-1)]
    return d

n = int(input())
l = list(map(int, input().split()))
print(*bike(l, n), sep=' ')