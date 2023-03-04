def solution(before, after):
    numb = []
    s = [*set(before)]
    for c in s:
        numb.append(before.count(c))
    for c in after:
        for t in range(len(s)):
            if c == s[t]:
                numb[t] -= 1
    for c in numb:
        if c != 0:
            return 0
    return 1

b = input()
a = input()
print(solution(b, a))