# 온라인 판매 -> 난 진짜 병신인가? 마음이 너무 급했던거 같음.
def price(money, n, m): #
    max = 0
    idx = 0
    for i in range(m):
        if (i+1) > n:
            now = money[i]*n
        else:
            now = money[i]*(i+1)
        if now > max:
            max = now
            idx = i
    return money[idx], max

n, m = map(int, input().split())
money = []
for _ in range(m):
    money.append(int(input()))
money.sort(reverse=True)
n, m = price(money, n, m)
print('{} {}'.format(n, m))