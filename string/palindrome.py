def find_pal(m, l):
    for i in range(len(l)//2):
        if l[i] != l[m-i-1]:
            return 0
    return l

def divide(str):
    for i in str:
        for j in range(n-m+1):
            out = find_pal(m, i[j:j+m])
            if out != 0:
                return out
    return out

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    str = [list(input()) for _ in range(n)]
    out = divide(str)
    if out == 0:
        for i in range(n):
            for j in range(i+1, n):
                str[i][j], str[j][i] = str[j][i], str[i][j]
        out = divide(str)
    print('#{} {}'.format(test_case, ''.join(out)))