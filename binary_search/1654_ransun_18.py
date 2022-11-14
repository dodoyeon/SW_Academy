def greedy_2(r_list, k, n):
    r_list.sort()
    max_l = r_list[-1]
    check = n
    while check > 0:
        check = n
        for i in range(k):
            check -= (r_list[k-i-1]//max_l)
            if check <= 0:
                return max_l
        max_l -= 1
    return max_l

def bin_search(r_list, k, n):
    start = 1
    end = max(r_list)
    while (end - start) >= 0:
        num = 0
        mid = (start + end)//2
        for i in range(k):
            num += (r_list[i]//mid)
        if num >= n:
            start = mid +1
        else:
            end = mid - 1
    return end


k, n = map(int, input().split())
r_list = [int(input()) for _ in range(k)]
print(bin_search(r_list, k, n))