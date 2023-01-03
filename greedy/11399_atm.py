# ATM
n = int(input())
plist = list(map(int, input().split()))
plist.sort()
sum = 0
psum = 0
for p in plist:
    psum += p
    sum += psum
print(sum)