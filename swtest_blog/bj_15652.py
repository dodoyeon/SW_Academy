n, m = map(int, input().split())
l = [(i+1) for i in range(n)]
result = [0]*m

def over_perm(l, n, m, level):
    if level == m:
        print(' '.join(str(i) for i in result))
        return
    for i in range(n):
        if level > 0:
            if l[i] >= result[level-1]:
                result[level] = l[i]
                over_perm(l, n, m, level + 1)
        else:
            result[level] = l[i]
            over_perm(l,n,m,level+1)

over_perm(l,n,m,0)