# 문자열 내 맘대로 정하기
def solution(strings, n):
    sdict = {}
    ans = []
    for i in strings:
        if i[n] in sdict.keys():
            sdict[i[n]].append(i)
        else:
            sdict[i[n]] = [i]
    for i in sorted(sdict.keys()):
        for j in sorted(sdict[i]):
            ans.append(j)
    return ans

def answersheet(strings, n):
    strings.sort()
    return sorted(strings, key= lambda x:x[n])

n = int(input())
l = list(input().split())
print(solution(l, n))