# Tetrahedral Stacks of Cannonballs
def canon(n):
    d = [0]*(n+1)
    d[1] = 1
    for i in range(2, n+1):
        d[i] = i*(i+1)//2
    return sum(d)

n = int(input())
for i in range(n):
    num = int(input())
    print('{}: {} {}'.format(i+1, num, canon(num)))