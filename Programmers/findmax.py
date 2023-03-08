# 가장 큰 수 찾기
def solution(array):
    idx, maxn = 0,0
    for i, c in enumerate(array):
        if maxn < c:
            maxn = c
            idx = i
    return [maxn, idx]

def answersheet(array):
    m = max(array)
    return [m, array.index(m)]