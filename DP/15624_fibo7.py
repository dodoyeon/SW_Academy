# 피보나치 수 7
def fibo(n):
    d = [0, 1]
    for _ in range(2, n+1):
        temp = sum(d)
        d[0], d[1] = d[1]%1000000007, temp%1000000007
    return d[1]
# 너무 큰 수를 계산하려고 해도 시간초과가 날 수 있다!!!

n = int(input())
print(fibo(n))