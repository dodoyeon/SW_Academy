# 밑과 같이 풀면 안됨 : 나누는 수인 5, 3, 2 가 서로 배수이지 않기 때문.
def make1(n):
    num = 0
    while n > 1:
        if n % 5 == 0:
            n //= 5
        elif n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1
        num += 1
    return num

def make2(n):
    num = 0
    d = [[] for _ in range(4)]
    while n > 1:
        if n % 5 == 0:
            d[0].append(n // 5)
        if n % 3 == 0:
            d[1].append(n // 3)
        if n % 2 == 0:
            d[2].append(n // 2)
        if:
            d[3].append(n - 1)
    return num

n = int(input())
print(make2(n))