def cal(l):
    # usun = {'+':0, '-':0, '*':1, '/':1}
    stack = []
    out = 0
    for i in l:
        # asc = ord(i[0])
        # if asc >= 48 and asc <= 57:
        if i.isnumeric():
            stack.append(i)
        elif i == '.':
            if len(stack) != 1:
                return 'error'
            return stack.pop()
        else:
            if len(stack) < 2:
                out = 'error'
                return out
            b = int(stack.pop())
            a = int(stack.pop())
            if i == '+':
                stack.append((a+b))
            elif i == '-':
                stack.append((a-b))
            elif i == '*':
                stack.append((a*b))
            elif i == '/':
                stack.append((a//b))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l = input().split()
    print('#{} {}'.format(test_case, cal(l)))