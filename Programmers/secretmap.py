# 비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        new1 = format(arr1[i], 'b').zfill(n)
        new2 = format(arr2[i], 'b').zfill(n)
        t = ''
        for j in range(n):
            if new1[j]== '1' or new2[j]=='1':
                t += '#'
            else:
                t += ' '
        answer.append(t)
    return answer

n = int(input())
a1 = list(map(int, input().split(', ')))
a2 = list(map(int, input().split(', ')))
print(solution(n, a1, a2))