def paline_othersolution(n):
    l = [0]*26
    count = 0
    right = ''
    temp = ''
    for i in n:
        idx = ord(i)-65
        l[idx] += 1
    for i in range(26):
        now = chr(i + 65)
        if l[i]%2 == 1:
            temp = now
            count+= 1
        for j in range(l[i]//2):
            right += now
    if count >= 2:
        return "I'm Sorry Hansoo"
    left = right[::-1]
    return right + temp + left
n = input()
print(paline_othersolution(n))