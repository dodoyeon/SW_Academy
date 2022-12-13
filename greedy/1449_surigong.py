# 수리공 항승
def number(n, l, where):
    nlist= []
    nlist.append(where[0])
    nlist.append(where[0] + (l - 1))
    for i in range(1, n):
        now = where[i]
        for i in range(len(nlist)-1, -1, -2):
           if now > nlist[i]:
               nlist.append(now)
               nlist.append(now + (l - 1))
               break
           elif nlist[i-1] <=now<=nlist[i]:
               break
    return len(nlist)//2

n, l = map(int, input().split())
where = list(map(int, input().split()))
where.sort()
print(number(n, l, where))