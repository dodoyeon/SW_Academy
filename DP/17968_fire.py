# Fire on Field
def fire(n):
    a = [0]*(n+1)
    a[0], a[1] = 1, 1
    for i in range(2, n+1):
        a[i] = min(a[])
    return a[n]

n = int(input())
print(fire(n))