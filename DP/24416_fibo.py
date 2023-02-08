num1, num2 = 0, 0
def fibo(n):
    global num1
    if n == 1 or n == 2:
        return 1
    num1 += 1
    return fibo(n-1)+fibo(n-2)

def fibonacci(n):
    global num2
    d = [0]*(n+1)
    d[1], d[2] = 1, 1
    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]
        num2 += 1
    return d[n]
n = int(input())
fibo(n)
fibonacci(n)
print('{} {}'.format(num1+1, num2))