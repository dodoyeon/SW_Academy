# 어케 푼건지 아리까리..
def elec(l, k, n, m):
    num = 0
    e = k
    idx = 0
    for i in range(1, n):
        e -= 1
        if i in l and idx < m-1:
            idx += 1
            if (l[idx]-i) > e:
                e = k
                num += 1
        elif i in l and idx == m-1:
            if (n - i) > e:
                e = k
                num += 1
        if e == 0:
            return 0
    return num

T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    l = list(map(int, input().split()))
    out = elec(l, k, n, m)
    print('#{} {}'.format(test_case, out))