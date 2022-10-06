# merge sort
def mergesort(l):


# quick sort
def quick(l, start, end):
    if start >= end:
        return
    n = len(l)
    pivot = l[end]
    i = start
    for j in range(start, end):
        if l[j] < pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i],l[end] = l[end], l[i]

def quicksort(l):
    quick(l, 0, len(l)-1)