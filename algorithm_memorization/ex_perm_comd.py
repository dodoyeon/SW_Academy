n = 4
m = 3
l = [1, 2, 3, 4]

p_result = [0]*m
p_visited = [False]*len(l)
def permutation(l, m, level):
    if level == m:
       print(p_result)
       return
    for i in range(len(l)):
        if p_visited[i] == False:
            p_visited[i] = True
            p_result[level] = l[i]
            permutation(l, m, level+1)
            p_visited[i] = False

c_result = [0]*m

def combination(l, m, level, idx):
    if level == m:
        print(c_result)
        return
    for i in range(idx, len(l)):
        c_result[level] = l[i]
        combination(l, m, level+1, i+1)

permutation(l, m, 0)
print('\\')
combination(l, m, 0, 0)