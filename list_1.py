# 1.
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n = int(input())
#     l = list(map(int, input().split()))
#     max_n = l[0]
#     min_n = l[0]
#     for i in l[1:]:
#         if i < min_n:
#              min_n = i
#         if i > max_n:
#              max_n = i
#     out = (max_n-min_n)
#     print('#{} {}'.format(T, out))

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    l = list(map(int, input().split()))
    num = 0
    elec = k
    i = 0
    j = 0
    while i <= n:
        elec -= 1
        i += 1
        if i < l[j] and elec > 0:
            pass
        elif i < l[j] and elec <=0:
            num = 0
            break
        if i >= l[j] and elec > 0:
            if (i+elec) < l[j+1]:
                num += 1
                j += 1
                i = l[j]
            elif (i+elec) == l[j+1]:
                num += 1
                j += 1
                i = l[j]
            else:
                num = 0
                break
    print('#{} {}'.format(test_case, num))

# 3.
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n=int(input())
#     num = input()
#     score = [0]*10
#     for i in range(n):
#         i = int(num[i])
#         score[i] += 1
#         m = max(score)
#     for i in range(9,0,-1):
#         if score[i] == m:
#             break
#     print('#{} {} {}'.format(test_case, i, m))

# 4.
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     l = list(map(int, input().split()))
#     start = 0
#     end = m
#     sum_l = []
#     while end <= n:
#         sum_l.append(sum(l[start:end]))
#         start += 1
#         end += 1
#     print('#{} {}'.format(test_case, (max(sum_l)-min(sum_l))))