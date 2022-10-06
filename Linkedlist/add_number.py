# 근데 linked list 를 사용하지는 않았다

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    num_list = list(map(int, input().split()))
    index = [i for i in range(n)]
    for i in range(m):
        idx, num = map(int, input().split())
        num_list.insert(idx, num)
    print("#{} {}".format(test_case, num_list[l]))