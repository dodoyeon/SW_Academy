# 알고리즘 수업- 피보나치 수 2
num1 = 0
def fibo(n):
    global num1
    if n==1 or n==2:
        return 1
    else:
        num1 += 1
        return fibo(n-1)+fibo(n-2)

def fibonacci(n):
    d = [0]*(n+1)
    d[1], d[2] = 1, 1
    num = 0
    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]
        num += 1
    return num

# 위처럼 무식하게 직접해보라는 뜻이 아닌거같다.
def fibonum(n):
    a, b = 1, 1
    # d = [0]*(n+1)
    # d[1], d[2] = 1, 1
    for _ in range(3, n+1):
        a, b = b, (a+b)%1000000007 # answer = b
    return b, (n-2)

n = int(input())
# fibo(n)
# print('{} {}'.format((num1+1)%1000000007, fibonacci(n)%1000000007))
print(*fibonum(n), sep=' ')
# 뭐가 문제인지는 모르겠는데 Python3 말고 pypy 로 내면 맞기는 한다....