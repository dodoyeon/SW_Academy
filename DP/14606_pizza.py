# 피자 (small)
# 7 - 4 3 - 2 2 2 1 -
# 9 - 5 4 - 2+1 2 2 2 - 1+1 1 11 11
# 10 - 5 5 - 3 2 3 2 - 2 1 11 2 1 11
#
def pizza(n):
    d = [0]*(n+1)
    num = 1
    idx, t = n//2, n%2
    d[n] = idx*(idx+t)
    while idx != 1:
        idx_next, t_next = idx // 2, idx % 2
        if t == 0:
            d[idx] = num*(idx_next*(idx_next+t_next))
        else:
            d[idx] += idx_next*(idx_next+t_next)
            d[idx+t] += idx_next*(idx_next+t_next)
        num *= 2
        idx, t = idx_next, t_next
    if t == 1:
        return sum(d)+1
    return sum(d)

n = int(input())
print(pizza(n))