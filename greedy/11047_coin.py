# 동전 0
n, k = map(int, input().split())
alist = [int(input()) for _ in range(n)]
alist.reverse()
# alist = alist[::-1]
# alist.sort(reverse=True) # 이렇게는 필요없다 이미 오름차순으로 입력되기때문
num = 0
for i in range(n):
    a = alist[i]
    if k>=a:
        num += k//a
        k = k%a
    # if k == 0:
    #     break
print(num)