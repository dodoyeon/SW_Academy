# 18353 병사 배치하기
def soldier(n, l):
    d = [0]*n
    for i in range(1, n):
        if l[i-1] <= l[i]:
            for j in range(i):
                if l[i] < l[j]:
                    d[i] = (i-j)
                    d[i+1] = d[i-1]
                    break
        else:
            d[i] = d[i-1]
    return min(d)

n = int(input())
l = list(map(int, input().split()))
print(soldier(n, l))