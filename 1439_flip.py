# 뒤집기
def flip(line):
    l = len(line)
    num = 0
    for i in range(1, l):
        if line[i] != line[i-1]:
            num += 1
    if line[0] != line[-1]:
        num += 1
    if num == 1:
        return 1
    return num//2

line = input()
print(flip(line))