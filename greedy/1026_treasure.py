def treasure(a, b, n):
    a.sort()
    b.sort(reverse=True)
    num = 0
    for i in range(n):
        num += (a[i]*b[i])
    return num
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = treasure(a, b, n)
print(ans)