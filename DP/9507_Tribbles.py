# Generations of Tribbles
def koong(n):
    if n < 2:
        return 1
    elif n == 2:
        return n
    elif n == 3:
        return 4
    d = [0]*(n+1)
    d[0], d[1], d[2], d[3] = 1, 1, 2, 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3] + d[i-4]
    return d[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(koong(n))