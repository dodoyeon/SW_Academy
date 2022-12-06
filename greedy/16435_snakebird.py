# 스네이크버드
def eat(n,l,height):
    for i in range(n):
        if height[i] <= l:
            l += 1
    return l

n, l = map(int, input().split())
height = list(map(int, input().split()))
height.sort()
print(eat(n,l,height))