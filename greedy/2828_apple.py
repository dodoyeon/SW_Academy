# 사과 담기 게임
def move(pos, n, m):
    start = 1
    end = m
    num = 0
    for a in pos:
        if start > a:
            c = (start-a)
            start -= c
            end -= c
            num += c
        elif a > end:
            c = (a-end)
            end += c
            start += c
            num += c
    return num
n, m = map(int, input().split())
j = int(input())
pos = []
for _ in range(j):
    pos.append(int(input()))
print(move(pos, n, m))