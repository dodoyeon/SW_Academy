from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
q = deque()
visited[0][0]=1
q.append([0,0])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while bool(q):
    for i in range(4):
        x, y =q.popleft()
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<m and miro[nx][ny]!=0 and visited[nx][ny] ==0:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])
print(visited[n-1][m-1])


# from collections import deque
# n, m = map(int, input().split())
# miro = [list(map(int, input())) for _ in range(n)]
#
# visited=[[0]*m for _ in range(n)]
# q = deque()
# # num = 0 # 움직인 칸 수
# dx = [-1, 0, 1, 0] # 다음에 갈 방향
# dy = [0, 1, 0, -1]
#
# q.append([0, 0])
# visited[0][0] = 1
#
# while bool(q):
#     x, y = q.popleft()
#     # num += 1
#     for i in range(4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]
#
#         # 배열의 범위 체크
#         # if next_x<0 or next_x>=n: continue # x가 배열의 범위를 넘었는지
#         # if next_y<0 or next_y>=m: continue # y 가 ''
#         # if miro[next_x][next_y] == 0: continue # 해당 좌표가 벽인지
#         # if visited[next_x][next_y] != 0 : continue # 한번 visit 한 곳인지
#
#         # 이렇게 해도됨
#         if 0<=next_x<n and 0<=next_y<m and miro[next_x][next_y] !=0 and visited[next_x][next_y]==0:
#             visited[next_x][next_y] = visited[x][y] + 1
#             q.append([next_x, next_y])
#
# print(visited[n-1][m-1])