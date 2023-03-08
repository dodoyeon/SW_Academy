def solution(s):
    ans = []
    adict = {}
    for i, c in enumerate(s):
        if c not in adict.keys():
            adict[c] = i
            ans.append(-1)
        else:
            ans.append(i-adict[c])
            adict[c] = i
    return ans

n= input()
print(solution(n))