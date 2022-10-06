# 어떻게 풀었는지 아리까리..
def comb_sum(l, n, k, level, idx, sum, num, visited):
    if level == n and sum == k:
        num += 1
        return num
    elif sum > k or level > n:
        return num
    for i in range(idx, len(l)-1):
        if k < l[i]:
            break
        else:
            sum += l[i]
            visited.append(l[i])
            num = comb_sum(l, n, k, level+1, idx+1, sum, num, visited)
            sum -= visited.pop()
    return num

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     n, k = map(int, input().split())
#     l = [(i+1) for i in range(12)]
#     sum = 0 # 더한 값
#     num = 0 # 부분집합 개수
#     visited = []
#     n = comb_sum(l, n, k, 0, 0, sum, num, visited)
#     print('#{} {}'.format(test_case, n))

import itertools
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    l = [(i+1) for i in range(12)]
    num = 0
    if k < l[-1]:
        l = l[:(k-1)]
    for i in itertools.combinations(l, n):
        if sum(i) == k:
            num += 1
    print('#{} {}'.format(test_case, num))