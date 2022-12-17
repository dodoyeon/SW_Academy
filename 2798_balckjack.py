# 블랙잭 : 브론즈2 = 이거는 코드 외워야하는데.. 까먹엇어ㅠㅜ 아마 permutation
def cardsum(n, m, card):
    maxc = 0

n, m = map(int, input())
card = []
for _ in range(n):
    card.append(int(input()))

print(cardsum(n, m, card))