def bin_search(r_list, k, n):
    start = 1
    end = max(r_list)
    while (end-start) >= 0:
        mid = (start+end)//2
        num = 0
        for i in r_list:
            num += (i//mid)
        if num >= n: # 최대 길이를 찾는 것이기 때문에 num = n 과 같으면 길이를 키운다.
            start = mid + 1
        elif num < n:
            end = mid - 1
    return end

k, n = map(int, input().split())
r_list = [int(input()) for _ in range(k)]
print(bin_search(r_list, k, n))