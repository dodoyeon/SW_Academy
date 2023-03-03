# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

def answersheet(my_str, n): # 내가 하고 싶었던 것.
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

n = int(input())
i = input()
print(answersheet(i, n))