def comb(plist, idx):
    global m, n, psum, tsum
    if psum > m:
        m = psum
    for i in range(idx, n):
        t, p = plist[i]
        if n >= (i + t) and (i + 1) > tsum:
            psum += p
            tsum += t
            comb(plist, i+1)
            psum -= p
            tsum -= t

def maybecomb(plist, n):
    global m, psum, tsum
    m, psum, tsum = 0, 0, 0
    comb(plist,  0)
    return m

n = int(input())
plist = []
for i in range(n):
    t, p = map(int, input().split())
    plist.append([t, p])

print(maybecomb(plist, n))