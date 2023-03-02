# PCCP 모의고사 1회
def solution1(input_string):
    cdict = {i:0 for i in range(97, 123)}
    tdict = {i:False for i in range(97, 123)}
    temp = ord(input_string[0])
    for c in input_string:
        idx = ord(c)
        cdict[idx] += 1
        if cdict[idx] >= 2 and temp != idx:
            tdict[idx] = True
        temp = idx
    answer = ''
    for i in range(97, 123):
        if tdict[i] == True:
            answer += chr(i)
    if answer == '':
        return 'N'
    return answer

# n = input()
# print(solution(n))

def solution(ability):
    n = len(ability[0]) # 종목
    m = len(ability) # 사람
    visited = []
    for j in range(m):
        for i in range(n):
            if visited[j] == False:
                visited[j] = True
                d[j][i] = ability[j][i]
        maxv = max(maxv, sum(d))
        visited = [False] * m
    return maxv

l = [list(map(int, input().split())) for _ in range(5)]
print(solution(l))

def solution3(queries):
    cdict = ['RR', 'Rr', 'Rr', 'rr']
    answer = []
    for q in queries:
        if q[0] == 1:
            answer.append('Rr')
        val = q[1]-1
        for i in range(q[0], 1, -1):
            mok = val// (4**(i-2))
            if mok == 0:
                answer.append('RR')
                break
            elif mok == 3:
                answer.append('rr')
                break
            if i == 2:
                answer.append(cdict[mok])
                break
            val %= (4**(i-2))
    return answer

# q = list(map(int, input().split()))
# print(solution(q))