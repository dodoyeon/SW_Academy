# example1
def traversal():
    l,c = map(int, input().split())
    l_2d = []
    out = []
    for i in range(l):
        l_2d.append(list(map(int, input().split())))
        for j in range(c):
            if l_2d[i][j] == 1:
                out.append(j)
    return out

# ex2
l_2d = [[1,2,3],[4,5,6],[7,8,9]]
l = len(l_2d)
for i in range(l):
    for j in range(i+1):
        l_2d[i][j], l_2d[j][i] = l_2d[j][i], l_2d[i][j]
print(l_2d)