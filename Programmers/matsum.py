# 행렬의 덧셈
def solution(arr1, arr2):
    l1, l2 = len(arr1), len(arr1[0])
    answer = [[0]*l2 for _ in range(l1)]
    for i in range(l1):
        for j in range(l2):
            answer[i][j] = arr1[i][j]+arr2[i][j]
    return answer

def answersheet(arr1, arr2):
    answer = []
    for ar, br in zip(arr1, arr2):
        answer.append([a+b for a, b in zip(ar, br)])
    return answer