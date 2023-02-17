# 연속부분최대곱
def maxmux(n, l):
    # d = [[0]*n for _ in range(2)]
    d = l
    for i in range(1, n):
        if d[i-1] > 1:
            d[i] = d[i-1]*d[i]
    return max(l)

n = int(input())
l = [float(input()) for _ in range(n)]
print(f'{maxmux(n, l):.3f}')