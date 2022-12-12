# 국회의원 선거
def maesu(n, cand):
    num = 0
    while True:
        count = 0
        for i in range(n-2, -1, -1):
            other = cand[i]
            me = cand[-1]
            if me < other:
                c = (other - me) // 2 + 1
                if c == 0:
                    c = 1
                cand[-1] += c
                cand[i] -= c
                num += c
                count += c
            elif me == other:
                cand[-1] += 1
                cand[i] -= 1
                num += 1
                count += 1
        if count == 0:
            return num

from collections import deque
def maesu_2(n, cand):
    q = deque()
    num = 0
    for i in range(n-2, -1, -1):
        if cand[-1] <= cand[i]:
            q.append(i)
    while q:
        i = q.popleft()
        other = cand[i]
        me = cand[-1]
        if me <= other:
            c = (other - me) // 2
            if c == 0:
                c = 1
            cand[-1] += c
            cand[i] -= c
            num += c
        if cand[i] > cand[-1]:
            q.append(i)

    return num

n = int(input())
me = int(input())
cand = []
for _ in range(n-1):
    cand.append(int(input()))
cand.sort()
cand.append(me)
print(maesu_2(n, cand))

tldldldldldlldlqkdkdkdkdkdkf ahfmrpTek tlqkf