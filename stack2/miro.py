def miro_path(miro, n, idx, next_x, next_y, next_val, visited, path_stack):
    move = [(1,0),(-1,0),(0,1),(0,-1)]

    while next_val != 3:
        nx = next_x + move[idx][0]
        ny = next_y + move[idx][1]
        next_val = miro[nx][ny]

        if (nx,ny) in visited or next_val == 1 or ((nx>=n) or (ny>=n)):
            past = path_stack.pop()
            next_x = past[0]
            next_y = past[1]
            next_val = miro[next_x][next_y]
            miro_path(miro, n, idx, next_x, next_y, next_val, visited, path_stack)
            idx = 0

        elif (nx, ny) not in visited and next_val == 0:
            next_x = nx
            next_y = ny
            visited.append((next_x, next_y))
            if (miro[next_x][next_y] == 0) or (miro[next_x][next_y] == 0):
                path_stack.append((next_x, next_y))

        else:
            return 0
    return 1



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    miro = []
    for i in range(n):
        miro.append([int(i) for i in input()])
    miro_flat = []
    for sub in miro:
        miro_flat.extend(sub)
    start = miro_flat.index(2)
    # start = miro[start // n][start % n]
    start_x = start // n
    start_y = start % n
    # end = miro_flat.index(3)
    # end = miro[end // n][end % n]
    # end_x = end//n
    # end_y = end%n
    path_stack = [(start_x, start_y)]
    visited = []
    miro_path(miro, n, 0, start_x, start_y,2, visited, path_stack)