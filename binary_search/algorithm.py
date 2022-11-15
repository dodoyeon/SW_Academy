def bin_search(l, a):
    l.sort()
    start = 0
    end = len(l)-1
    while (end-start) <= 0:
        mid = (start + end) // 2
        if l[mid] == a:
            return mid
        elif l[mid] > a:
            start = mid+1
        else:
            end = mid -1
    return -1

def bin_search_recur(l, a, start, end):
    if (end-start) < 0:
        return -1
    mid = (start + end) // 2
    if l[mid] == a:
        return mid
    elif l[mid] > a:
        start = mid + 1
        bin_search_recur(l, a, start, end)
    else:
        end = mid - 1
        bin_search_recur(l, a, start, end)