def name(a, b):
    h = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    new = []
    for i in range(len(a)):
        new.append(h[ord(a[i])-65])
        new.append(h[ord(b[i])-65])

    while len(new) > 2:
        temp = []
        for i in range(len(new)-1):
            temp.append((new[i]+new[i+1])%10)
        new = temp
    return new
a = input()
b = input()
print(*name(a, b), sep='')