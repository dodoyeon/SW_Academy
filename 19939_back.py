# 박 터트리기
def back_2(n, k):
    val = k*(k+1)//2
    cha = k-1
    if n < val:
        return -1
    elif n == val:
        return cha
    else:
        nam = (n - val)
        if nam%k == 0:
            return cha
        else:
            return cha + 1

# def back(n, k): # 반례 10 4, 11 4
#     pivot = n // k
#     move = k // 2
#     if pivot > move:
#         nam = n%k
#         if nam == 0:
#             return move*2
#         else:
#             return move*2+1
#     else:
#         return -1

n, k = map(int, input().split())
print(back_2(n, k))