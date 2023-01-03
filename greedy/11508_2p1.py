# 2+1 세일
n = int(input())
plist = []
for _ in range(n):
    plist.append(int(input()))

plist.sort(reverse=True)
sum = 0
for i in range(n):
    if i%3 == 2:
        pass
    else:
        sum += plist[i]
print(sum)