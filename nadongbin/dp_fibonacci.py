# 일반 재귀 함수
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

# d = [0]*101
# def fibo_dp1(n):
#     if n <= 1:
#         return n
#     if d[n] != 0:
#         return d[n]
#     d[n] = fibo_dp1(n-1)+fibo_dp1(n-2)
#     return d[n]
#
# def fibo_dp2(n):
#     d = [0]*(n+1)
#     d[1], d[2] = 1, 1
#     for i in range(3, n+1):
#         d[i] = d[i-1]+d[i-2]
#     return d[n]

# recursive
d1 = [0] * 101 # (n+1)
d1[1] = 1
def fibo_dp1(n):
    # print(n)
    if n <= 1:
        return d1[n]
    if d1[n] != 0:
        return d1[n]
    else:
        d1[n] = fibo_dp1(n-1) + fibo_dp1(n-2)
        return d1[n]

# iterative
def fibo_dp2(n):
    d = [0]*(n+1)
    d[1], d[2] = 1, 1
    for i in range(3, n+1):
        if d[i] != 0: # for 문이라서 필요없음
            return d[i]
        else:
            d[i] = d[i-1]+d[i-2]
    return d[n]
x = 10
# print(fibo(x))
print(fibo_dp1(x))
print(fibo_dp2(x))