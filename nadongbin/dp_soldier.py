# 18353 병사 배치하기
def soldier(n, l):
    d = [0]*n
    for i in range(1, n):
        if l[i] > l[i-1]:
            d[i] = d[i-1]+1
    return sum(d)

n = int(input())
l = list(map(int, input().split()))
print(soldier(n, l))