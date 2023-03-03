# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while chicken >= 10:
        mok, nam = chicken//10, chicken%10
        chicken = (mok+nam)
        answer += mok
    return answer

print(solution(int(input())))