#알바생 강호
def starbox(n, l):
    num = 0
    for i in range(n):
        val = (l[i] - (i))
        if val > 0:
            num += val
    return num

    return num
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort(reverse = True)
print(starbox(n, l))