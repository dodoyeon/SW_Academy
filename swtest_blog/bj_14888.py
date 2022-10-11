n = int(input())
nlist = list(map(int, input().split()))
tool = list(map(int, input().split()))
minn = int(1e9)
maxn = int(-1e9)
out = nlist[0]
pr = []

def dfs(nlist, tool, i):
    global out
    global minn, maxn
    global pr

    if i == len(nlist):
        if minn > out:
            minn = out
        if maxn < out:
            maxn = out
        # print(pr)
        return

    temp = out
    for j in range(4):
        if tool[j] > 0:
            if j == 0:
                out += nlist[i]
                # pr.append('+')
            elif j == 1:
                out -= nlist[i]
                # pr.append('-')
            elif j == 2:
                out *= nlist[i]
                # pr.append('*')
            elif j == 3:
                # pr.append('/')
                if out <0:
                    t = (-out)//nlist[i]
                    out = -t
                else:
                    out = out // nlist[i]
            tool[j] -= 1
            dfs(nlist, tool, i + 1)
            out = temp
            tool[j] += 1
            # pr.pop()

dfs(nlist, tool, 1)
print(maxn)
print(minn)