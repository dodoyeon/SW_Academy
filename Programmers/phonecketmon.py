# 폰켓몬
def solution(nums):
    s = set(nums)
    l = len(nums)//2
    ans=l if l < len(s) else len(s)
    return ans

def answersheet(nums):
    return min(len(set(nums)), len(nums)//2)