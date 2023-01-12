# 피보나치를 DP 로 풀어보기
def pibo_recur(n):
    if n <= 1:
        return n
    else:
        return pibo_recur(n-1)+pibo_recur(n-2)

def dp(n):
    dpmem = [0, 1]
    if n >= 2:
        for i in range(2, (n+1)):
            dpmem.append(dpmem[i-1]+dpmem[i-2])
    return dpmem[n]
n = int(input())
print(dp(n))