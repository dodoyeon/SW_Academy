# 수들의 합
def numsum(s, e, goal):
    mid = (s + e) // 2
    val = (mid) * (mid + 1) // 2
    if val > goal:
        e = mid
        mid = numsum(s, e, goal)
    elif val < goal:
        val = (mid+1) * (mid + 2) // 2
        if val > goal:
            return mid
        elif val == goal:
            return mid+1
        else:
            s = mid
            mid = numsum(s, e, goal)
    return mid

e = int(input())
mid = (1+e)//2
value = mid*(mid+1)//2
print(numsum(1, e, e))