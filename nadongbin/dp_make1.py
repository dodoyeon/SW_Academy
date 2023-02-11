# 밑과 같이 풀면 안됨 : 나누는 수인 5, 3, 2 가 서로 배수이지 않기 때문.
def make1_answersheet(n):
    d = [0]*(n+1)
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i%5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    return d[n]

def make2(n):
    d = [i for i in range(n, -1, -1)]
    for i in range(n, 0, -1):
        # d[i-1] = d[i]+1
        if i % 2 == 0:
            d[i//2] = min(d[i]+1, d[i//2])
        if i % 3 == 0:
            d[i // 3] = min(d[i] + 1, d[i // 3])
        if i % 5 == 0:
            d[i // 5] = min(d[i] + 1, d[i // 5])
    return d[1]

n = int(input())
print(make2(n))