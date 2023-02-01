# def dp(n, nlist): # 일단 for 문을 써야하는 거 같은데..
#     d = [0]*n
#     visited = [False]*n
#     n0 = nlist[0]
#     n1 = nlist[1]
#     if n0 >= n1:
#         d[0], d[1] = n0, n0
#         visited[0] = True
#     else:
#         d[0], d[1] = 0, n1
#         visited[1] = True
#     for i in range(2, n):# n-1, -1, -1
#         if d[i-2]+nlist[i] < d[i-1]:
#             d[i] = d[i - 2] + nlist[i]
#             visited[i] = True
#             if i != 0 and visited[i-1] == True:
#                 visited[i - 1] = False
#     return d[n]
#
# n = int(input())
# nlist = list(map(int, input().split()))
# print(dp(n, nlist))

# arr = [2,1,3,1,4,2,1,3]
# def sol(arr):
#     d = [arr[0]]
#     m = []
#     for i in range(1, len(arr)):
#         val = arr[i]
#         for j in range(i):
#             if d[j] != val:
#                 d.append(val)
#             else:
#                 m.append((i - j))
#     if len(m) == 0:
#         return -1
#     else:
#         return min(m)
# print(sol(arr))

# def solution(arr, n):
#     for i in arr:
#         if (n - i) in arr:
#             return True
#     return False
#
# def solution(arr, n):
#     arr.sort()
#     al = len(arr)
#     for i in range(al):
#         val = arr[i]
#         if val < n:
#             for j in range(i, al):
#                 if (n-val) == arr[j]:
#                     return True
#     return False

import math
anslist = []
def comb(nlist, m, level, idx):
    if level == idx:
        anslist.append(num)
    for i in range(idx, len(nlist)):
        num += nlist[i]
        comb(nlist, m, level + 1, i + 1)

def solution(bunjje):
    dl, n = 1, 1
    list3 = [1]
    while True:
        for j in range(n):
            dl += math.comb(n, j)
            val = 3**n
            list3.append(val)
            if dl >= (bunjje-1):
                return comb(list3, (bunjje-dl), 0, 0)

# print(solution(4))

# x = input()
# resa, res1 = '',''
# for c in x:
#   if 65 <= ord(c) <= 90:
#     resa += c
#   else:
#     res1 += c
# resa = sorted(list(resa))
# res1 = sorted(list(res1))
# print(''.join(resa)+''.join(res1))

def dduck(dlist, n, m):
    global res
    num = 0
    mid = (0+dlist[0])//2
    for i in range(n):
        d = dlist[i]
        if mid <= d:
           num += (d-mid)
    if num == m:
        if res < mid:
            res = mid
    elif num < m:
        dduck(dlist, n, m)
    else:
        res.append(l)
        dduck(dlist, rlist[:mid], n, m)
    return dlist[i]
