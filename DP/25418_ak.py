# 정수 a 를 k로 만들기
def ak(a, k):
    d = [0]*(k+1)
    for i in range(k-1, a-1, -1):
        d[i] = d[i+1]+1
        if i*2 <= k:
            d[i] = min(d[i*2]+1, d[i])
    return d[a]

a, k = map(int, input().split())
print(ak(a, k))