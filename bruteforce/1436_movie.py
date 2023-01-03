# 1436 영화감독 숌
def title(n): # 브루트포스는 이런식으로 푼다
    num = 0
    now = 666
    while True:
        if '666' in str(now):
            num += 1
        if num == n:
            return now
        now += 1

n = int(input())
print(title(n))