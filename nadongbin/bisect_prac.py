from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
l = list(map(int, input().split()))

left = bisect_left(l, x)
right = bisect_right(l, x)
print(right-left)