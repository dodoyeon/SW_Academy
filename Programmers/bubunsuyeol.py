# 크기가 작은 부분문자열
def solution(t, p):
    lp = len(p)
    p = int(p)
    answer = 0
    for i in range(len(t)-lp+1):
        if int(t[i:i+lp])<=p:
            answer += 1
    return answer

t = input()
p = input()
print(solution(t, p))