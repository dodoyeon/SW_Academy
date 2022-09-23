T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1=input()
    str2 = input()
    num = []
    for i in str1:
        n = 0
        for j in str2:
            if i == j:
                n +=0
        num.append(n)
    print('#{} {}'.format(test_case, max(num)))