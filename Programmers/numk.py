# k의 개수
def solution(i, j, k):
    t = ''.join(str(n) for n in range(i, j+1))
    return t.count(str(k))

i, j, k = map(int, input().split())
print(solution(i, j, k))