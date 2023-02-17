# Cow Solitaire
from collections import deque
def cow(n, mapp, start):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    score = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    q = deque()
    d = [0]*(2*n-2)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    return

n = int(input())
mapp = [list(input.split())for _ in range(n)]
print(cow(n, mapp, (n-1, 0)))