# 3.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    num = input()
    score = [0]*10
    for i in range(n):
        i = int(num[i])
        score[i] += 1
        m = max(score)
    for i in range(9,0,-1):
        if score[i] == m:
            break
    print('#{} {} {}'.format(test_case, i, m))