# 돌 게임
def stone(n):
    if n%2 == 0:
        return 'CY'
    return 'SK'

def stone_dp(n):
    d = [0]*1001 # [0]*(n+1) 이 낫지 않나?
    d[1], d[2], d[3] = 1,0,1 # 1개나 3개 남았을 때
    for i in range(4, n+1):
        if d[i-1] or d[i-3]:
            d[i] = 0
        else:
            d[i] = 1
    return ('CY' if d[n] == 0 else 'SK')

n = int(input())
print(stone_dp(n))