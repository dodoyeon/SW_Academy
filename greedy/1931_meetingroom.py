# 회의실 배정
def dfs(now, num):


n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    if i != 0:
        for j in range(i):
            meeting.insert(j, list(s, e))
    else:
        meeting.append(list(s, e))
m = 0
dfs(0, 0)
print()