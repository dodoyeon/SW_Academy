# 돌 게임
def stone(n):
    if n%2 == 0:
        return 'CY'
    return 'SK'

def stone_dp(n):
    pass

n = int(input())
print(stone(n))