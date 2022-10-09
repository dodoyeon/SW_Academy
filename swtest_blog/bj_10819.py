n = int(input())
l = list(map(int, input().split()))


max = 0
def perm_sum(l,n,level, perm_result, out, visited):
    if level == n:
        perm_out = out[:] #copy
        perm_result.append(perm_out)
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            out[level] = l[i]
            perm_sum(l,n,level+1, perm_result, out, visited)
            visited[i] = False

def permutation(l,n):
    perm_result = []
    out = [0] * n
    visited = [False] * n
    perm_sum(l,n,0, perm_result, out, visited)
    return perm_result

perm_result = permutation(l,n)

for list in perm_result:
    sum_out = 0
    for idx in range(1, n):
        sum_out += abs(list[idx-1]-list[idx])
    if max < sum_out:
        max = sum_out
print(max)