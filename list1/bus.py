T = int(input())
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    l = list(map(int, input().split()))
    num = 0
    elec = k
    i = 0
    j = 0
    while i <= n:
        elec -= 1
        i += 1
        if i < l[j] and elec > 0:
            pass
        elif i < l[j] and elec <=0:
            num = 0
            break
        if i >= l[j] and elec > 0:
            if (i+elec) < l[j+1]:
                num += 1
                j += 1
                i = l[j]
            elif (i+elec) == l[j+1]:
                num += 1
                j += 1
                i = l[j]
            else:
                num = 0
                break
    print('#{} {}'.format(test_case, num))