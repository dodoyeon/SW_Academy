# 라디오
def radio(a, b, l):
    minn = abs(a-b)
    for c in l :
        num = abs(c-b)+1
        if minn > num:
            minn = num
    return minn

a, b = map(int, input().split())
n = int(input())
cha = []
for _ in range(n):
    cha.append(int(input()))
print(radio(a, b, cha))