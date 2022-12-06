# 컵홀더
n = int(input())
seat = list(input())
num = 1
for i in range(n):
    if seat[i] == 'S':
        num += 1
    else:
        num += 0.5
if num > n:
    print(n)
else:
    print(int(num))