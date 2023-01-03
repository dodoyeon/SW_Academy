# 회의실 배정
n = int(input())
meeting = []
for _ in range(n-1):
    l = list(map(int, input().split()))
    t = l[1]-l[0]
    l.append(t)
    meeting.append(l)
