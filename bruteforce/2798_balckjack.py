# 블랙잭 : 브론즈2 = 이거는 코드 외워야하는데.. 까먹엇어ㅠㅜ 아마 permutation
def combination(n, m, level, idx, card):
    global c
    global maxc
    if level == 3:
        s = sum(c)
        if s <= m and s > maxc:
            maxc = s
        return
    for i in range(idx, n):
        c[level] = card[i]
        combination(n, m, level+1, i+1, card)

def comb(n,m,card):
    global c
    global maxc
    maxc = 0
    c = [0] * 3
    combination(n, m, 0, 0, card)

n, m = map(int, input().split())
card = list(map(int, input().split()))
comb(n, m, card)
print(maxc)