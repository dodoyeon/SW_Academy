# 피보나치 수 7
def fibo(n):
    a, b = 0, 1
    if n == 0 or n == 1:
        return n
    for _ in range(2, n+1):
        a, b = b%1000000007, (a+b)%1000000007
    return b
# 너무 큰 수를 계산하려고 해도 시간초과가 날 수 있다!!!

n = int(input())
print(fibo(n))