# 백준 : 피보나치 수열 문제와 같다.
def fibo(x):
    d = [0]*(x+1)
    d[0] = 1
    if x == 0:
        return d[0]
    d[1] = 1
    for i in range(2, x+1):
        d[i] = d[i-1]+d[i-2]
    return d[x]

n = int(input())
for _ in range(n):
    num = int(input())
    print(fibo(num))