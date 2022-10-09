n = int(input())

# 완전 permutation 함수
def perm(l, n, level, result, visited):
    if level == n:
        print(' '.join(str(i) for i in result))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result[level] = l[i]
            perm(l, n, level + 1, result, visited)
            visited[i] = False

def permutation(n):
    result = [0] * n
    visited = [False] * n
    l = [(i + 1) for i in range(n)]
    perm(l, n, 0, result, visited)

permutation(n)