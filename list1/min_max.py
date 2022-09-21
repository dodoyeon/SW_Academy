# 1.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    l = list(map(int, input().split()))
    max_n = l[0]
    min_n = l[0]
    for i in l[1:]:
        if i < min_n:
             min_n = i
        if i > max_n:
             max_n = i
    out = (max_n-min_n)
    print('#{} {}'.format(T, out))