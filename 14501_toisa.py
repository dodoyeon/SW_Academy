# 퇴사
n = int(input())
plist = []
for i in range(n):
    t, p = map(int, input().split())
    if n >= (i + t):
        plist.append([t, p])
m = 0
p = len(plist)
for i in range(p):
    psum = 0
    tsum = 0
    for j in range(i, p):
        t = plist[j][0]
        if (j+1) > tsum:
            psum += plist[j][-1]
            tsum = j+t
    if psum > m:
        m = psum
print(m)