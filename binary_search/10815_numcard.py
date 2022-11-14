# 숫자 카드
# def search(have, sear): # 시간 초과가 뜬다!
#     ans = []
#     for i in sear:
#         if i in have:
#             ans.append(1)
#         else:
#             ans.append(0)
#     return ans

# 그래서 이진탐색을 사용해야 한다.
# -> 근데 얘도 시간초과남; : 왜냐하면 bin_search() 함수에 have.sort() 를 햇어서 그랫다..
def bin_search(have, s):
    start = 0
    end = len(have)-1
    while (end-start) >= 0:
        mid = (start+end)//2
        if have[mid] > s:
            end = mid - 1
        elif have[mid] < s:
            start = mid + 1
        else:
            return 1
    return 0

def search_s(have, sear):
    res = []
    have.sort()
    for s in sear:
        ans = bin_search(have, s)
        res.append(ans)
    return res

n = int(input())
have = list(map(int, input().split()))
m = int(input())
sear = list(map(int, input().split()))
ans = search_s(have, sear)
print(' '.join(str(i) for i in ans))