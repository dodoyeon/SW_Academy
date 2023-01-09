# 홀수일까 짝수일까
n = int(input())
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        print('even')
    else:
        print('odd')