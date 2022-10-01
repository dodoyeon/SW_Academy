def bracket(l):
    stack = []
    for i in l:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) ==0 or stack.pop() != '(':
                return 0
        elif i == '}':
            if len(stack) ==0 or stack.pop() != '{':
                return 0
        elif i == ']':
            if len(stack) ==0 or stack.pop() != '[':
                return 0
    if len(stack) != 0:
        return 0
    return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l = input()
    out = bracket(l)
    print('#{} {}'.format(test_case, out))