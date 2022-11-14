# 괄호 : 비슷한 문제를 푼 적 있음
# 큐가 아니라 스택으로 풀어야 함!!
from collections import deque
def VPS(line):
    stack = deque()
    for i in line:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                j = stack.pop()
            else:
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    return 'YES'

n = int(input())
for _ in range(n):
    line = list(input())
    print(VPS(line))