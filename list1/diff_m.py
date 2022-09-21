# 4.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    start = 0
    end = m
    sum_l = []
    while end <= n:
        sum_l.append(sum(l[start:end]))
        start += 1
        end += 1
    print('#{} {}'.format(test_case, (max(sum_l)-min(sum_l))))