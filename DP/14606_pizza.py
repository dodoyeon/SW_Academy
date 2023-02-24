# 피자 (small)
# 7 - 4 3 - 2 2 2 1 -
# 9 - 5 4 - 2+1 2 2 2 - 1+1 1 11 11
# 10 - 5 5 - 3 2 3 2 - 2 1 11 2 1 11
#
def pizza(n):
    if n == 1:
        return 0
    d = [[0]*(n+1) for _ in range(2)]
    mok = n//2
    d[0][n] = mok*(n-mok)
    d[1][mok] += 1
    d[1][n - mok] += 1
    for i in range(n-1, 0, -1):
        if d[1][i] >= 1:
            mok = i//2
            d[0][i] += d[1][i]*mok*(i-mok)
            d[1][mok] += d[1][i]
            d[1][i-mok] += d[1][i]
    return sum(d[0])

n = int(input())
print(pizza(n))