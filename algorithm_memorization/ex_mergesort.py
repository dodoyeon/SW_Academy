# merge sort
def mergesort(l):
    n = len(l)
    if n <=1:
        return

    mid = n//2
    l1 = l[:mid]
    l2 = l[mid:]
    mergesort(l1)
    mergesort(l2)

    il = 0
    i1 = 0
    i2 = 0
    while i1<len(l1) and i2<len(l2):
        if l1[i1] < l2[i2]:
            l[il] = l1[i1]
            i1 += 1
            il += 1
        else:
            l[il] = l2[i2]
            i2 += 1
            il += 1

    while i1<len(l1):
        l[il] = l1[i1]
        i1 += 1
        il += 1
    while i2<len(l2):
        l[il] = l2[i2]
        i2 += 1
        il += 1

# quick sort
def quick(l, start, end):
    if start >= end:
        return

    pivot = l[end]
    i = start
    for j in range(start, end):
        if l[j] < pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i],l[end] = l[end], l[i]
    quick(l, start, i-1)
    quick(l, i+1, end)

def quicksort(l):
    quick(l, 0, len(l)-1)