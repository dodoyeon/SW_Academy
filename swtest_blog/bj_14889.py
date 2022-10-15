n= int(input())
s = [list(map(int, input().split())) for _ in range(n)]
minx = 1e8
def cal(s, l, n):
    out = 0
    for k in range(n):
        for j in range(k,n):
            a = l[k]
            b = l[j]
            out += (s[a][b] + s[b][a])
    return out

def dfs(mid, s, start, level,idx):
    global minx
    if level == mid:
        link = [item for item in range(n) if item not in start]
        out1 = cal(s, start, mid)
        out2 = cal(s, link, mid)
        out1 = abs(out1-out2)
        if out1 < minx:
            minx = out1
        return

    for i in range(idx, mid*2):
        start[level] = i
        dfs(mid,s,start,level+1,i+1)

def dfs_st(n, s):
    global minx
    mid = n // 2
    start = [0] * mid

    dfs(mid, s,start, 0, 0)
    print(minx)

dfs_st(n, s)