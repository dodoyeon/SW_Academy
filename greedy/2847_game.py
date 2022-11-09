# 게임을 만든 동준이
n = int(input())
score = [int(input()) for _ in range(n)]
num = 0
for i in range(n-1, 0, -1):
    prev = score[i-1]
    now = score[i]
    if prev >= now:
        score[i-1] = now-1
        num += (prev-now+1)
print(num)