# 부분수열의 합 - 백트래킹 방법
def back_tracking(idx, res):
    global cnt
    if idx >= n:
        return
    res += k[idx]
    if res == s:
        cnt += 1

    back_tracking(idx+1, res) # 현재값을 포함하는 경우
    back_tracking(idx+1, res-k[idx]) # 현재값을 빼는 경우

n, s = map(int, input().split())
k =list(map(int, input().split()))
cnt = 0 # 부분수열의 개수
back_tracking(0, 0)
print(cnt)
# 다시하기!!