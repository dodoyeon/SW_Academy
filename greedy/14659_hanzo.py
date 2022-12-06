# 14659 한조서열정리하고옴ㅋㅋ -> 2중 for 문으로 풀면 시간초과
n = int(input())
bong = list(map(int, input().split()))
num = []
pivot = bong[0]
count = 0
for i in range(1, n):
    if bong[i] < pivot:
        count += 1
    else:
        pivot = bong[i]
        num.append(count)
        count = 0
num.append(count)
print(max(num))