# Polynesiaglot (Small1)
from itertools import product
mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm?
def poly(c, v, l):
    element = [i for i in range(c+v)]
    cons = [i for i in range(c)]
    case = list(product(element, repeat = 2))
    num = len(case)
    for i in case:
        for idx, e in enumerate(i):
            if e in cons and i[idx-1] :
                num -= 1
    return num

t= int(input())
for i in range(t):
    c, v, l = map(int, input().split())
    print('Case #{}: {}'.format(i, poly(c, v, l)))