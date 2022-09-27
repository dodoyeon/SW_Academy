T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    c1 = set()
    c2 = set()
    for i in range(n):
        x1,y1,x2,y2,c = map(int, input().split())
        if c == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    c1.add((i,j))
        else:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    c2.add((i,j))
    print('#{} {}'.format(test_case, len(c1&c2)))