# 숫자카드 2
# 이런식으로 while 안에 while 또 넣어서 계산하면 시간초과난다........
def bin_search(have, end, s, n):
    num = 0
    start = 0
    while (end-start) >= 0:
        mid = (start+end)//2
        if have[mid] > s:
            end = mid - 1
        elif have[mid] < s:
            start = mid + 1
        else:
            r_mid = mid
            l_mid = mid
            while r_mid >= 0 and have[r_mid] == s:
                num +=1
                r_mid -= 1
            while l_mid < n and have[l_mid] == s:
                num +=1
                l_mid += 1
            return num-1
    return num

def bin_search2(have, s, n):
    start = 0
    end = n - 1
    while (end-start) >= 0:
        mid = (start+end)//2
        if have[mid] > s:
            end = mid-1
        elif have[mid] < s:
            start = mid + 1
        else:
            return mid
    return -1

def search_s(have, sear, n):
    have.sort()
    res = []
    for s in sear:
        ans = bin_search2(have, s, n)
        if ans != -1:
            res.append(have.count(have[ans]))
        else:
            res.append(0)
    return res

n = int(input())
have = list(map(int, input().split()))
m = int(input())
sear = list(map(int, input().split()))
ans = search_s(have, sear, n)
print(' '.join(str(i) for i in ans))