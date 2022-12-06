# 캠핑 (브론즈 1)
def greed(l, p, v):
    res = (v//p)*l
    m = v%p
    if m <= l:
        return res + m
    return res + l
i = 0
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v == 0:
        break
    i += 1
    res = greed(l, p, v)
    print("Case {}: {}".format(i, res))