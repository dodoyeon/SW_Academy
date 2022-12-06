# 수들의 합
def numsum(s, num):
    g = num*(num+1)//2
    if g > s:
        numsum(s, num-1)
    elif g < s:
        numsum(s, num+1)
    else:
        return num

s = int(input())
print(numsum(s, s//3))