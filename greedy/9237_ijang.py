# 이장님 초대
def invite(tree, n):
    num = tree[0]
    for t in range(1, n):
        next_t = (tree[t] + t)
        if num < next_t:
            num = next_t
    return num+2
n = int(input())
tree = list(map(int,input().split()))
tree.sort(reverse=True)
print(invite(tree, n))