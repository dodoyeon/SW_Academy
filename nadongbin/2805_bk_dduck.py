def binsearch_imp(l, m):
    s, e = 0, l[-1]
    res = 0
    while (e-s) >= 0:
        mid = (s+e)//2
        num = 0
        for i in l:
            if i > mid:
                num += (i - mid)
        if num == m:
            s = mid+1
            if res < mid:
                res = mid
        elif num < m:
            e = mid-1
        else:
            s = mid+1
            if res < mid:
                res = mid
    return res

def binsearch(l, val):
   s, e = 0, len(l)-1
   while (e-s) >= 0:
       mid = (s+e)//2
       if l[mid] == val:
           return mid
       elif l[mid] < val:
           e = mid - 1
       else:
           s = mid + 1

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(binsearch_imp(l, m))