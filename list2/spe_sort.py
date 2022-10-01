def merge_sort(l):
    n = len(l)
    if n <= 1:
        return
    mid = n//2
    l1 = l[:mid]
    l2 = l[mid:]
    merge_sort(l1)
    merge_sort(l2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1<len(l1) and i2<len(l2):
        if l1[i1] > l2[i2]:
            l[ia] = l1[i1]
            ia += 1
            i1 += 1
        else:
            l[ia] = l2[i2]
            ia += 1
            i2 += 1

    while i1<len(l1):
        l[ia] = l1[i1]
        ia += 1
        i1 += 1
    while i2<len(l2):
        l[ia] = l2[i2]
        ia += 1
        i2 += 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    l = list(map(int, input().split()))
    merge_sort(l)
    mid = n//2
    new = l[:mid+1]
    for i in range(n-1, mid,-1):
        new.insert(2*(n-i)-1, l[i])
    print('#{} {}'.format(test_case, ' '.join(str(i) for i in new[:10])))