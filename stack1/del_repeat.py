T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str = input()
    stack = []
    for c in str:
        if len(stack) != 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    out = len(stack)
    if out == 0:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, out))